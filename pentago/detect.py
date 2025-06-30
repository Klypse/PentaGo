# 2024-11-29 Kiri, All rights reserved.
from pentago.lang import *
from pentago.api import *
from pentago.client import *
from pentago.hash import Crypto
from pentago.response import Response
import httpx

class Detect:
    def __init__(self, query: str) -> None:
        self.query = query
    
    async def lang(self) -> str:
        crypto = Crypto(API_DECT)
        headers = {
            **CLIENT_HEADER,
            'authorization': crypto.authorization,
            'timestamp': crypto.timestamp,
            'referer': API_BASE
        }
        async with httpx.AsyncClient() as client:
            res = await client.post(API_DECT, headers=headers, data=dict(query=self.query))
        status = Response(res.status_code)
        if status.response:
            content = res.json()
            lang = content['langCode']
            if lang != 'unk':
                return lang