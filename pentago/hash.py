# 2025-07-04 Klypse, MIT License
"""
Pure‑blocking cryptographic helper.  It is only responsible for
producing an authorization header.  Heavy/ blocking work is off‑loaded by
calling code through crypto_async() in utils.py, so we keep this file
synchronous and simple.
"""
import base64
import hmac
import time
import uuid
from pathlib import Path

_DIGEST_MOD = "MD5"
_LICENSE_CACHE: str | None = None  # in‑memory cache – file read only once

def reset_license_cache():
    global _LICENSE_CACHE
    _LICENSE_CACHE = None


class Crypto:
    """Calculate device‑dependent authorization header for Pentago API."""

    def __init__(self, text: str):
        self.text = text
        self._device_id: str | None = None
        self._timestamp: str | None = None
        self._hash: str | None = None
        self._authorization: str | None = None

    @property
    def key(self) -> str:
        global _LICENSE_CACHE
        if _LICENSE_CACHE is None:
            try:
                _LICENSE_CACHE = Path("license_key.txt").read_text()
            except FileNotFoundError:
                from pentago.update import Software
                Software().update()
                _LICENSE_CACHE = Path("license_key.txt").read_text()
        return _LICENSE_CACHE

    @property
    def device_id(self) -> str:
        if self._device_id is None:
            self._device_id = str(uuid.uuid4())
        return self._device_id

    @property
    def timestamp(self) -> str:
        if self._timestamp is None:
            self._timestamp = str(int(time.time() * 1000))
        return self._timestamp

    @property
    def hash(self) -> str:
        if self._hash is None:
            message = f"{self.device_id}\n{self.text}\n{self.timestamp}".encode()
            digest = hmac.digest(self.key.encode(), message, _DIGEST_MOD)
            self._hash = base64.b64encode(digest).decode()
        return self._hash

    @property
    def authorization(self) -> str:
        if self._authorization is None:
            self._authorization = f"PPG {self.device_id}:{self.hash}"
        return self._authorization