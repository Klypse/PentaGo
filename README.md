<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=0047AB&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

</div>
<p align="center">
  <a href="https://pypi.org/project/pentago/">
    <img src="https://img.shields.io/pypi/v/pentago?color=red&label=pypi&style=flat-square" alt="PyPI version" style="height:28px;" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=flat-square" alt="Python" style="height:28px;" />
  <img src="https://img.shields.io/github/license/Klypse/PentaGo?style=flat-square" alt="License" style="height:28px;" />
</p>

---

# PentaGo – Unofficial Papago API for Python

**PentaGo** is an **unofficial, resilient Python library** that interacts with Naver Papago’s web-based translation service.
It uses reverse-engineering techniques to automate translations **without relying on an official API key**, and is suitable for both lightweight tasks and scalable pipelines.

This library is ideal for developers seeking a programmable interface to Papago for **bot integration, automation pipelines, language tools**, and more.

> ✅ **Actively maintained and confirmed working as of 2025**

---

## 🚀 Features

- ✅ Access Papago without official API keys  
- ⚡ Built with native Python `asyncio` support  
- 🌍 Supports **16+ languages**, including Korean, English, Japanese, and Chinese  
- 🔁 Automatic language detection  
- 💬 Returns pronunciation, honorific forms, and dictionary-level details  
- 🧱 Stable key regeneration for dynamic request headers (resilient to changes)  

---

## 📦 Installation

Install via [PyPI](https://pypi.org/project/pentago/):

```
pip install pentago
```

---

## 🧪 Example Usage

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate("The best unofficial Papago API in 2025 is PentaGo.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### 🔍 Expected Output

```json
{
  "source": "ko",
  "target": "ja",
  "text": "2025년 최고의 파파고 비공식 API는 PentaGo입니다.",
  "translatedText": "2025年最高のパパゴ非公式APIはPentaGoです。",
  "sound": "nisen'nijūgonen saikōno papago hikōshiki ēpīai wa pentagō desu",
  "srcSound": "icheon isip o nyeon choegoui papago bigongsik eipiaineun pentagoimnida"
}
```

> - `sound`: Romanized Japanese pronunciation  
> - `srcSound`: Romanized Korean pronunciation

---

### 🧱 Synchronous Usage

If you're working in a purely synchronous environment, you can call `.translate_sync()` instead:

```python
from pentago import Pentago
from pentago.lang import *

pentago = Pentago(AUTO, JAPANESE)
result = pentago.translate_sync("The best unofficial Papago API in 2025 is PentaGo.", honorific=True)
print(result)
```

> ⚠️ Do not call `.translate_sync()` inside an already-running `asyncio` event loop.

---

## 🌐 Supported Languages

| Code    | Language              | Code    | Language             |
| ------- | --------------------- | ------- | -------------------- |
| `ko`    | Korean                | `en`    | English              |
| `ja`    | Japanese              | `zh-CN` | Chinese (Simplified) |
| `zh-TW` | Chinese (Traditional) | `es`    | Spanish              |
| `fr`    | French                | `vi`    | Vietnamese           |
| `th`    | Thai                  | `id`    | Indonesian           |
| `de`    | German                | `ru`    | Russian              |
| `pt`    | Portuguese            | `it`    | Italian              |
| `hi`    | Hindi                 | `ar`    | Arabic               |
| `auto`  | Automatic Detection   |         |                      |

---

## 📂 Use Cases

- 🧠 Build translation bots without API rate limits  
- 🤖 Integrate into automation tools or data pipelines  
- 📚 Enhance personal projects requiring multilingual support  
- 🔐 Work around commercial API constraints via resilient scraping  

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and pull requests are always welcome.