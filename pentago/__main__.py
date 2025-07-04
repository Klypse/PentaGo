# 2025-07-04 Klypse, MIT License
from typing import Dict, Optional
import json
import httpx

from pentago.api import *
from pentago.client import *
from pentago.detect import Detect
from pentago.response import Response
from pentago.utils import crypto_async
from pentago.hash import Crypto


class Pentago:
    """Asynchronous translator with lazy crypto+language detection caching."""

    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        self._crypto: Optional[Crypto] = None  # instance‑level cache

    # --------------------------------------------------------------
    #  Public API
    # --------------------------------------------------------------
    async def translate(
        self, text: str, honorific: bool = False, verbose: bool = False
    ) -> Dict[str, str]:
        """Translate *text* from *source* to *target* asynchronously."""

        # auto‑detect source language once per call
        if self.source == "auto":
            detected = await Detect(text).lang()
            if detected:
                self.source = detected

        # lazily create Crypto for translation endpoint
        if self._crypto is None:
            self._crypto = await crypto_async(API_TRANS)

        body = {
            "authorization": self._crypto.authorization,
            "timestamp": self._crypto.timestamp,
            "deviceId": self._crypto.device_id,
        }
        headers = {
            **CLIENT_HEADER,
            **body,
            "referer": API_BASE,
            "x-apigw-partnerid": API_ID,
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(
                API_TRANS,
                headers=headers,
                data={
                    **body,
                    "locale": "ko",
                    "dict": "true",
                    "dictDisplay": "30",
                    "honorific": str(honorific).lower(),
                    "instant": "false",
                    "paging": "true",
                    "source": self.source,
                    "target": self.target,
                    "text": text,
                },
            )
        status = Response(res.status_code)
        if status.response:
            content = res.json()
            if verbose: return json.dumps(content, indent=4)
            sound: str = None
            srcSound: str = None
            if 'tlit' in content:
                sound = ' '.join(list(map(lambda x: x['phoneme'], content['tlit']['message']['tlitResult'])))
            if 'tlitSrc' in content:
                srcSound = ' '.join(list(map(lambda x: x['phoneme'], content['tlitSrc']['message']['tlitResult'])))
            return {
                'source': self.source,
                'target': self.target,
                'text': text,
                'translatedText': content['translatedText'],
                'sound': sound,
                'srcSound': srcSound
            }