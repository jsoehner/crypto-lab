"""Mature External Key Management (EKM / HYOK) Control Plane Reference.

Demonstrates the Hold-Your-Own-Key (HYOK) / Cloud EKM architecture (used by
GCP Cloud EKM, Azure Confidential/EKM proxies, HashiCorp Vault KMIP, and
Thales CipherTrust):
  - Root Key Encryption Keys (KEKs) NEVER leave the external KMS/HSM boundary.
  - Cloud workloads hold only an external key URI (`ekm://...`) and send
    authenticated wrap/unwrap requests with caller identity & justification AAD.
  - The external KMS enforces policy, records immutable audit logs, and provides
    an instant cryptographic kill-switch (`disable_key` / `destroy_key`) that
    immediately blocks cloud decryption even if cloud storage is compromised.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from crypto_support import random_bytes


class KeyState(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DESTROYED = "DESTROYED"


@dataclass(frozen=True)
class AuditEvent:
    timestamp: str
    key_uri: str
    operation: str
    caller: str
    justification: str
    allowed: bool
    reason: str


@dataclass
class ExternalKeyRecord:
    key_uri: str
    material: bytes
    allowed_callers: set[str]
    state: KeyState = KeyState.ENABLED


class ExternalKmsControlPlane:
    """Sovereign external KMS/HSM enforcing policy, audit logging, and instant revocation."""

    def __init__(self) -> None:
        self._keys: dict[str, ExternalKeyRecord] = {}
        self.audit_log: list[AuditEvent] = []

    def create_key(self, key_id: str, allowed_callers: set[str]) -> str:
        key_uri = f"ekm://kms.corp.internal/v0/keys/{key_id}"
        self._keys[key_uri] = ExternalKeyRecord(
            key_uri=key_uri,
            material=random_bytes(32),
            allowed_callers=set(allowed_callers),
        )
        self._record(key_uri, "CREATE", "kms-admin", "provision", True, "Key created inside external KMS")
        return key_uri

    def disable_key(self, key_uri: str, actor: str, reason: str) -> None:
        record = self._require_key(key_uri)
        if record.state == KeyState.DESTROYED:
            raise PermissionError("Cannot disable a destroyed key")
        record.state = KeyState.DISABLED
        self._record(key_uri, "DISABLE", actor, reason, True, "Key disabled (cryptographic kill-switch)")

    def enable_key(self, key_uri: str, actor: str, reason: str) -> None:
        record = self._require_key(key_uri)
        if record.state == KeyState.DESTROYED:
            raise PermissionError("Cannot re-enable a destroyed key")
        record.state = KeyState.ENABLED
        self._record(key_uri, "ENABLE", actor, reason, True, "Key re-enabled")

    def destroy_key(self, key_uri: str, actor: str, reason: str) -> None:
        record = self._require_key(key_uri)
        record.state = KeyState.DESTROYED
        record.material = b"\x00" * len(record.material)
        self._record(key_uri, "DESTROY", actor, reason, True, "Key material zeroized")

    def remote_wrap(self, key_uri: str, dek: bytes, caller: str, justification: str) -> bytes:
        record = self._authorize(key_uri, "WRAP", caller, justification)
        nonce = random_bytes(12)
        aad = f"{key_uri}|{justification}".encode("utf-8")
        return nonce + AESGCM(record.material).encrypt(nonce, dek, aad)

    def remote_unwrap(self, key_uri: str, wrapped_dek: bytes, caller: str, justification: str) -> bytes:
        record = self._authorize(key_uri, "UNWRAP", caller, justification)
        nonce, ct = wrapped_dek[:12], wrapped_dek[12:]
        aad = f"{key_uri}|{justification}".encode("utf-8")
        return AESGCM(record.material).decrypt(nonce, ct, aad)

    def _require_key(self, key_uri: str) -> ExternalKeyRecord:
        if key_uri not in self._keys:
            raise KeyError(f"Unknown EKM key URI: {key_uri}")
        return self._keys[key_uri]

    def _authorize(self, key_uri: str, op: str, caller: str, justification: str) -> ExternalKeyRecord:
        record = self._require_key(key_uri)
        if record.state != KeyState.ENABLED:
            self._record(key_uri, op, caller, justification, False, f"Key state is {record.state.value}")
            raise PermissionError(f"EKM access denied: key {key_uri} is {record.state.value}")
        if caller not in record.allowed_callers:
            self._record(key_uri, op, caller, justification, False, "Caller not in allowlist")
            raise PermissionError(f"EKM access denied: unauthorized caller {caller}")
        if not justification.strip():
            self._record(key_uri, op, caller, justification, False, "Missing access justification")
            raise PermissionError("EKM access denied: justification required")
        self._record(key_uri, op, caller, justification, True, "Authorized")
        return record

    def _record(
        self,
        key_uri: str,
        operation: str,
        caller: str,
        justification: str,
        allowed: bool,
        reason: str,
    ) -> None:
        self.audit_log.append(
            AuditEvent(
                timestamp=datetime.now(timezone.utc).isoformat(),
                key_uri=key_uri,
                operation=operation,
                caller=caller,
                justification=justification,
                allowed=allowed,
                reason=reason,
            )
        )


@dataclass(frozen=True)
class EkmEnvelope:
    key_uri: str
    wrapped_dek: bytes
    nonce: bytes
    ciphertext: bytes


def cloud_encrypt_with_ekm(
    ekm: ExternalKmsControlPlane,
    key_uri: str,
    plaintext: bytes,
    aad: bytes,
    caller: str,
    justification: str,
) -> EkmEnvelope:
    """Cloud workload generates DEK locally and asks the external KMS to wrap it."""
    dek = random_bytes(32)
    wrapped_dek = ekm.remote_wrap(key_uri, dek, caller=caller, justification=justification)
    nonce = random_bytes(12)
    ciphertext = AESGCM(dek).encrypt(nonce, plaintext, aad)
    return EkmEnvelope(key_uri=key_uri, wrapped_dek=wrapped_dek, nonce=nonce, ciphertext=ciphertext)


def cloud_decrypt_with_ekm(
    ekm: ExternalKmsControlPlane,
    envelope: EkmEnvelope,
    aad: bytes,
    caller: str,
    justification: str,
) -> bytes:
    """Cloud workload requests remote unwrap from the external KMS."""
    dek = ekm.remote_unwrap(envelope.key_uri, envelope.wrapped_dek, caller=caller, justification=justification)
    return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    ekm = ExternalKmsControlPlane()
    caller = "spiffe://prod-cloud/ns/payments/sa/checkout"
    key_uri = ekm.create_key("payments-root-kek", allowed_callers={caller})

    aad = b"bucket=prod-ledger;object=tx-991"
    envelope = cloud_encrypt_with_ekm(
        ekm, key_uri, b"regulated financial record", aad, caller=caller, justification="CUSTOMER_INITIATED_WRITE"
    )
    recovered = cloud_decrypt_with_ekm(
        ekm, envelope, aad, caller=caller, justification="CUSTOMER_INITIATED_WRITE"
    )
    assert recovered == b"regulated financial record"

    # Demonstrate instant sovereign kill-switch
    ekm.disable_key(key_uri, actor="secops-oncall", reason="incident-containment")
    print(f"ExternalKmsEkmExample OK keyUri={key_uri} auditEvents={len(ekm.audit_log)}")


if __name__ == "__main__":
    main()
