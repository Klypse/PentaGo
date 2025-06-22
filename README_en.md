<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

📘 [한국어](./README.md) | 🌍 [English](./README_en.md) | 🇯🇵 [日本語](./README_ja.md) | 🇫🇷 [Français](./README_fr.md) | 🇩🇪 [Deutsch](./README_de.md) | 🇻🇳 [Tiếng Việt](./README_vi.md) | 🇸🇦 [العربية](./README_ar.md)
</div>

---

# 🧠 PentaGo

**PentaGo** is an unofficial Python translation library using the Naver Papago web interface asynchronously.  
It provides full translation features without requiring an API key.

> ✅ **Confirmed working in 2025**

---

## 🚀 Features

- ✅ **Unofficial Papago API wrapper**
- ⚡ **Async support (`async/await`)**
- 🌍 **Supports 16 languages**
- 💬 **Pronunciation & dictionary info**
- 🙇 **Honorific mode available**

---

## 📦 Installation

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 Example

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

| Code   | Language       | Code   | Language       |
|--------|----------------|--------|----------------|
| `ko`   | Korean         | `en`   | English        |
| `ja`   | Japanese       | `zh-CN`| Chinese (Simplified) |
| `zh-TW`| Chinese (Traditional) | `es` | Spanish |
| `fr`   | French         | `vi`   | Vietnamese     |
| `th`   | Thai           | `id`   | Indonesian     |
| `de`   | German         | `ru`   | Russian        |
| `pt`   | Portuguese     | `it`   | Italian        |
| `hi`   | Hindi          | `ar`   | Arabic         |
| `auto` | Auto Detect    |        |                |

---

## 📄 License

This project is licensed under [MIT](LICENSE).

---

## 🤝 Contributing

Pull requests and issues are always welcome.
