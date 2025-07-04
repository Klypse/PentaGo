# 2025-07-04 Klypse, MIT License
from typing import Optional
import httpx

from pentago.api import *
from pentago.client import *
from pentago.response import Response
from pentago.utils import crypto_async
from pentago.hash import Crypto


class Detect:
    """Language detector that caches Crypto at class level."""

    _crypto: Optional[Crypto] = None  # class‑wide shared cache

    def __init__(self, query: str):
        self.query = query

    async def _ensure_crypto(self) -> Crypto:
        if Detect._crypto is None:
            Detect._crypto = await crypto_async(API_DECT)
        return Detect._crypto

    async def lang(self) -> str | None:
        crypto = await self._ensure_crypto()
        headers = {
            **CLIENT_HEADER,
            "authorization": crypto.authorization,
            "timestamp": crypto.timestamp,
            "referer": API_BASE,
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(API_DECT, headers=headers, data={"query": self.query})
        status = Response(res.status_code)
        if status.response:
            content = res.json()
            lang = content['langCode']
            if lang != 'unk':
                return lang