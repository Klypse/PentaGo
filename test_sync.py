# 2024-11-29 Kiri, All rights reserved.
from pentago import Pentago
from pentago.lang import *
import asyncio

def translate(text):
    pentago = Pentago(AUTO, JAPANESE)
    res = pentago.translate_sync(text, honorific=True)
    print(res)

if __name__ == '__main__':
	translate(input('Enter text: '))
