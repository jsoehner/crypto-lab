"""Thales CipherTrust Manager Community Edition (REST API) EKM / Envelope Client.

Supports two modes:
  1. Live Mode: Set `CIPHERTRUST_URL` (e.g. `https://cm-ce.lab.internal`) and
     `CIPHERTRUST_USER` / `CIPHERTRUST_PASSWORD` (or `CIPHERTRUST_TOKEN`), plus
     optional `CIPHERTRUST_CA_BUNDLE` / mTLS client cert env vars.
  2. Offline Simulator Mode (default when `CIPHERTRUST_URL` is unset): Uses an
     in-memory protocol-compatible mock of CipherTrust's `/api/v1/vault/keys2`
     and `/api/v1/crypto/{encrypt,decrypt}` endpoints for CI and local demos.
"""

from __future__ import annotations

import base64
import json
import os
import ssl
import urllib.request
from dataclasses import dataclass
from typing import Any, Protocol

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from crypto_support import random_bytes


class CipherTrustTransport(Protocol):
    """Transport interface for CipherTrust Manager REST API calls."""

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]: ...


class LiveCipherTrustTransport:
    """HTTPS transport using stdlib urllib + optional mTLS for live CipherTrust Manager."""

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        ca_bundle: str | None = None,
        client_cert: str | None = None,
        client_key: str | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.ssl_ctx = ssl.create_default_context(cafile=ca_bundle) if ca_bundle else ssl.create_default_context()
        if client_cert and client_key:
            self.ssl_ctx.load_cert_chain(certfile=client_cert, keyfile=client_key)
        self.token = token
        if not self.token and username and password:
            auth = self.request(
                "POST",
                "/api/v1/auth/tokens",
                {"grant_type": "password", "username": username, "password": password},
            )
            self.token = auth["jwt"]

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        req = urllib.request.Request(f"{self.base_url}{path}", data=body, headers=headers, method=method)
        with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}


class SimulatedCipherTrustTransport:
    """Offline protocol-compatible simulator of CipherTrust Manager REST API."""

    def __init__(self) -> None:
        self._keys: dict[str, dict[str, Any]] = {}

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        payload = payload or {}
        if method == "POST" and path == "/api/v1/vault/keys2":
            name = payload["name"]
            key_id = f"cm-key-{len(self._keys) + 1}"
            self._keys[name] = {"id": key_id, "name": name, "material": random_bytes(32), "state": "Active"}
            return {"id": key_id, "name": name, "algorithm": "AES", "size": 256, "state": "Active"}

        if method == "POST" and path.startswith("/api/v1/vault/keys2/") and path.endswith("/deactivate"):
            key_name = path.split("/")[5]
            self._keys[key_name]["state"] = "Deactivated"
            return {"name": key_name, "state": "Deactivated"}

        if method == "POST" and path == "/api/v1/crypto/encrypt":
            record = self._require_active(payload["id"])
            nonce = random_bytes(12)
            aad = base64.b64decode(payload.get("aad", "")) if payload.get("aad") else b""
            pt = base64.b64decode(payload["plaintext"])
            ct_and_tag = AESGCM(record["material"]).encrypt(nonce, pt, aad)
            ct, tag = ct_and_tag[:-16], ct_and_tag[-16:]
            return {
                "id": record["id"],
                "ciphertext": base64.b64encode(ct).decode("ascii"),
                "iv": base64.b64encode(nonce).decode("ascii"),
                "tag": base64.b64encode(tag).decode("ascii"),
            }

        if method == "POST" and path == "/api/v1/crypto/decrypt":
            record = self._require_active(payload["id"])
            nonce = base64.b64decode(payload["iv"])
            ct = base64.b64decode(payload["ciphertext"])
            tag = base64.b64decode(payload["tag"])
            aad = base64.b64decode(payload.get("aad", "")) if payload.get("aad") else b""
            pt = AESGCM(record["material"]).decrypt(nonce, ct + tag, aad)
            return {"plaintext": base64.b64encode(pt).decode("ascii")}

        raise ValueError(f"Unsupported simulated endpoint: {method} {path}")

    def _require_active(self, key_name: str) -> dict[str, Any]:
        if key_name not in self._keys:
            raise KeyError(f"Key not found in CipherTrust: {key_name}")
        record = self._keys[key_name]
        if record["state"] != "Active":
            raise PermissionError(f"CipherTrust key {key_name} is {record['state']}")
        return record


class CipherTrustClient:
    """High-level CipherTrust Manager client for key lifecycle and DEK wrapping."""

    def __init__(self, transport: CipherTrustTransport) -> None:
        self.transport = transport

    @classmethod
    def from_env(cls) -> "CipherTrustClient":
        url = os.environ.get("CIPHERTRUST_URL")
        if not url:
            return cls(SimulatedCipherTrustTransport())
        return cls(
            LiveCipherTrustTransport(
                base_url=url,
                token=os.environ.get("CIPHERTRUST_TOKEN"),
                username=os.environ.get("CIPHERTRUST_USER"),
                password=os.environ.get("CIPHERTRUST_PASSWORD"),
                ca_bundle=os.environ.get("CIPHERTRUST_CA_BUNDLE"),
                client_cert=os.environ.get("CIPHERTRUST_CLIENT_CERT"),
                client_key=os.environ.get("CIPHERTRUST_CLIENT_KEY"),
            )
        )

    def create_aes256_key(self, name: str) -> dict[str, Any]:
        return self.transport.request(
            "POST",
            "/api/v1/vault/keys2",
            {"name": name, "algorithm": "AES", "size": 256, "undeletable": False, "unexportable": True},
        )

    def deactivate_key(self, name: str) -> dict[str, Any]:
        return self.transport.request("POST", f"/api/v1/vault/keys2/{name}/deactivate", {})

    def wrap_dek(self, key_name: str, dek: bytes, aad: bytes) -> dict[str, str]:
        return self.transport.request(
            "POST",
            "/api/v1/crypto/encrypt",
            {
                "id": key_name,
                "mode": "GCM",
                "plaintext": base64.b64encode(dek).decode("ascii"),
                "aad": base64.b64encode(aad).decode("ascii"),
            },
        )

    def unwrap_dek(self, key_name: str, wrapped: dict[str, str], aad: bytes) -> bytes:
        resp = self.transport.request(
            "POST",
            "/api/v1/crypto/decrypt",
            {
                "id": key_name,
                "mode": "GCM",
                "ciphertext": wrapped["ciphertext"],
                "iv": wrapped["iv"],
                "tag": wrapped["tag"],
                "aad": base64.b64encode(aad).decode("ascii"),
            },
        )
        return base64.b64decode(resp["plaintext"])


@dataclass(frozen=True)
class CipherTrustEnvelope:
    key_name: str
    wrapped_dek: dict[str, str]
    nonce: bytes
    ciphertext: bytes


def encrypt_with_ciphertrust(
    client: CipherTrustClient,
    key_name: str,
    plaintext: bytes,
    aad: bytes,
) -> CipherTrustEnvelope:
    dek = random_bytes(32)
    wrapped_dek = client.wrap_dek(key_name, dek, aad)
    nonce = random_bytes(12)
    ciphertext = AESGCM(dek).encrypt(nonce, plaintext, aad)
    return CipherTrustEnvelope(key_name=key_name, wrapped_dek=wrapped_dek, nonce=nonce, ciphertext=ciphertext)


def decrypt_with_ciphertrust(
    client: CipherTrustClient,
    envelope: CipherTrustEnvelope,
    aad: bytes,
) -> bytes:
    dek = client.unwrap_dek(envelope.key_name, envelope.wrapped_dek, aad)
    return AESGCM(dek).decrypt(envelope.nonce, envelope.ciphertext, aad)


def main() -> None:
    client = CipherTrustClient.from_env()
    key_name = "demo-app-kek"
    client.create_aes256_key(key_name)

    aad = b"tenant=ciphertrust-ce;purpose=envelope"
    env = encrypt_with_ciphertrust(client, key_name, b"ciphertrust protected payload", aad)
    pt = decrypt_with_ciphertrust(client, env, aad)
    assert pt == b"ciphertrust protected payload"
    mode = "live" if os.environ.get("CIPHERTRUST_URL") else "simulated"
    print(f"CipherTrustEkmExample OK mode={mode} keyName={key_name}")


if __name__ == "__main__":
    main()
