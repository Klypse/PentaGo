# 2025-07-04 Klypse, MIT License
import asyncio
from pentago.hash import Crypto

# Async wrapper that executes Crypto (which is blocking) in a thread pool
async def crypto_async(text: str) -> Crypto:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, Crypto, text)