<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

</div>

---

# 🧠 PentaGo

**PentaGo** is an unofficial Python translation library that interacts asynchronously with the **Naver Papago web interface**.  
It offers full translation functionality without requiring any API key.

> ✅ **Confirmed working as of 2025**  
> Regularly maintained to follow the latest structure of Papago's web service.

---

## 🚀 Features

- ✅ **Unofficial Papago API wrapper**
- ⚡ **Asynchronous support via `async/await`**
- 🌍 **Supports 16 languages**
- 💬 **Returns pronunciation & dictionary info**
- 🙇 **Honorific mode supported**

---

## 📦 Installation

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

> This project is not distributed via PyPI. Clone the repo directly to use.

---

## 🧪 Usage Example

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate("PentaGo is the best unofficial Papago API in 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### Sample Output:
```json
{
  "source": "en",
  "target": "ja",
  "text": "PentaGo is the best unofficial Papago API in 2025.",
  "translatedText": "2025年最高のパパゴ非公式APIはPentaGoです。",
  "sound": "nisen nijūgonen saikō no papago hikōshiki ēpīai wa pentago desu",
  "srcSound": "pentago is the best unofficial papago api in twenty twenty five"
}
```

---

## 🌐 Supported Languages

| Code | Language    | Code | Language     |
|------|-------------|------|--------------|
| ko   | Korean      | en   | English      |
| ja   | Japanese    | zh-CN| Chinese (Simplified) |
| zh-TW| Chinese (Traditional) | es | Spanish |
| fr   | French      | vi   | Vietnamese   |
| th   | Thai        | id   | Indonesian   |
| de   | German      | ru   | Russian      |
| pt   | Portuguese  | it   | Italian      |
| hi   | Hindi       | auto | Auto Detect  |

---

## 📁 Project Structure

```
PentaGo/
├── pentago/
│   ├── __init__.py
│   ├── main.py        # Core async logic
│   └── lang.py        # Language code constants
└── examples/
    └── basic.py       # Usage example
```

---

## 📄 License

This project is licensed under [GPL-3.0](LICENSE).

---

## 🤝 Contributing

- Pull requests and issues are welcome!
- Feel free to contribute features, bugfixes, or improvements.

---

<div align="center">

💡 _PentaGo is a sleek, unofficial API implementation that makes Papago accessible to developers._  
🌐 _Fast. Flexible. No API key required._

</div>
