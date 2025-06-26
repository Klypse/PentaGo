<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />


</div>

---

# 🧠 PentaGo

**PentaGo** is an unofficial asynchronous Python translation library utilizing Naver Papago's web interface. It provides reliable, high-performance translations without requiring an official API key.

> ✅ **Confirmed working as of 2025**

---

## 🚀 Features

* ✅ **Unofficial Papago API wrapper**
* ⚡ **Async support (`async/await`)**
* 🌍 **Supports 16 languages**
* 💬 **Includes pronunciation & dictionary details**
* 🙇 **Honorific language support**

---

## 📦 Installation

[![PyPI - Version](https://img.shields.io/pypi/v/pentago?color=red\&label=pip\&style=flat-square)](https://pypi.org/project/pentago/)

```bash
pip install pentago
```

---

## 🧪 Usage Example

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

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Issues and pull requests are welcome!
