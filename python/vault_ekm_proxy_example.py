"""OIDC + mTLS EKM Proxy Client (HashiCorp Vault Transit Pattern, absorbed from ekm-demo).

Demonstrates the three-layer External Key Manager (EKM) proxy pattern:
  - Layer 7 (Application): Bearer JWT validated against OIDC JWKS (Keycloak).
  - Layer 4 (Transport): Mutual TLS (mTLS) between the EKM Proxy and Vault.
  - Layer 1 (Data): Vault Transit KEK wraps/unwraps local AES-256-GCM DEKs.

Supports live mode when `EKM_PROXY_URL` and `EKM_JWT_TOKEN` are set, or runs
against `SimulatedVaultEkmProxy` in offline CI and local demos.
"""

from __future__ import annotations

import base64
import json
import os
import time
import urllib.request
from dataclasses import dataclass
from typing import Protocol

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from crypto_support import random_bytes


class EkmProxyTransport(Protocol):
    def wrap_dek(self, dek: bytes, jwt_token: str) -> str: ...
    def unwrap_dek(self, ciphertext: str, jwt_token: str) -> bytes: ...


class LiveVaultEkmProxyTransport:
    """HTTPS/HTTP client for the `ctm-ekm-lab/vault-oidc-proxy` service."""

    def __init__(self, proxy_url: str) -> None:
        self.proxy_url = proxy_url.rstrip("/")

    def wrap_dek(self, dek: bytes, jwt_token: str) -> str:
        # Vault Transit ciphertext is produced by Vault or proxy wrap endpoint
        req = urllib.request.Request(
            f"{self.proxy_url}/wrap-key",
            data=json.dumps({"plaintext_dek": base64.b64encode(dek).decode("ascii")}).encode("utf-8"),
            headers={"Authorization": f"Bearer {jwt_token}", "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))["ciphertext"]

    def unwrap_dek(self, ciphertext: str, jwt_token: str) -> bytes:
        req = urllib.request.Request(
            f"{self.proxy_url}/unwrap-key",
            data=json.dumps({"ciphertext": ciphertext}).encode("utf-8"),
            headers={"Authorization": f"Bearer {jwt_token}", "Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            b64 = json.loads(resp.read().decode("utf-8"))["plaintext_dek"]
            return base64.b64decode(b64)


class SimulatedVaultEkmProxy:
    """Offline simulator of Keycloak OIDC JWT + Rate-Limited EKM Proxy + Vault Transit."""

    def __init__(self, valid_tokens: set[str], max_requests_per_window: int = 10) -> None:
        self._vault_kek = random_bytes(32)
        self._valid_tokens = set(valid_tokens)
        self._max_requests = max_requests_per_window
        self._timestamps: list[float] = []

    def _check_policy(self, jwt_token: str) -> None:
        now = time.time()
        self._timestamps = [t for t in self._timestamps if now - t < 60.0]
        if len(self._timestamps) >= self._max_requests:
            raise RuntimeError("429 Too Many Requests: EKM proxy rate limit exceeded")
        self._timestamps.append(now)

        if jwt_token not in self._valid_tokens:
            raise PermissionError("401 Unauthorized: invalid or expired OIDC JWT")

    def wrap_dek(self, dek: bytes, jwt_token: str) -> str:
        self._check_policy(jwt_token)
        nonce = random_bytes(12)
        ct = AESGCM(self._vault_kek).encrypt(nonce, dek, b"vault:v1:my-master-kek")
        return "vault:v1:" + base64.b64encode(nonce + ct).decode("ascii")

    def unwrap_dek(self, ciphertext: str, jwt_token: str) -> bytes:
        self._check_policy(jwt_token)
        if not ciphertext.startswith("vault:v1:"):
            raise ValueError("Invalid Vault Transit ciphertext format")
        raw = base64.b64decode(ciphertext[len("vault:v1:") :])
        nonce, ct = raw[:12], raw[12:]
        return AESGCM(self._vault_kek).decrypt(nonce, ct, b"vault:v1:my-master-kek")


@dataclass(frozen=True)
class VaultProxyEnvelope:
    wrapped_dek_ciphertext: str
    nonce: bytes
    ciphertext: bytes


def encrypt_with_ekm_proxy(
    transport: EkmProxyTransport,
    jwt_token: str,
    plaintext: bytes,
    aad: bytes,
) -> VaultProxyEnvelope:
    dek = random_bytes(32)
    wrapped = transport.wrap_dek(dek, jwt_token)
    nonce = random_bytes(12)
    ct = AESGCM(dek).encrypt(nonce, plaintext, aad)
    return VaultProxyEnvelope(wrapped_dek_ciphertext=wrapped, nonce=nonce, ciphertext=ct)


def decrypt_with_ekm_proxy(
    transport: EkmProxyTransport,
    jwt_token: str,
    envelope: VaultProxyEnvelope,
    aad: bytes,
) -> bytes:
    dek = transport.unwrap_dek(envelope.wrapped_dek_ciphertext, jwt_token)
    return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    proxy_url = os.environ.get("EKM_PROXY_URL", "")
    jwt_token = os.environ.get("EKM_JWT_TOKEN", "demo-oidc-jwt-alice")
    transport: EkmProxyTransport = (
        LiveVaultEkmProxyTransport(proxy_url)
        if proxy_url
        else SimulatedVaultEkmProxy(valid_tokens={jwt_token})
    )

    aad = b"realm=ekm-demo;kek=my-master-kek"
    env = encrypt_with_ekm_proxy(transport, jwt_token, b"vault transit protected payload", aad)
    pt = decrypt_with_ekm_proxy(transport, jwt_token, env, aad)
    assert pt == b"vault transit protected payload"
    mode = f"live ({proxy_url})" if proxy_url else "simulated"
    print(f"VaultEkmProxyExample OK mode={mode}")


if __name__ == "__main__":
    main()
