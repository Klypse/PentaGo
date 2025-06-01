<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Asynchrone+Papago+Inoffizielle+API" alt="PentaGo Ticker" />

📘 [한국어](./README.md) | 🌍 [English](./README_en.md) | 🇯🇵 [日本語](./README_ja.md) | 🇫🇷 [Français](./README_fr.md) | 🇩🇪 [Deutsch](./README_de.md) | 🇻🇳 [Tiếng Việt](./README_vi.md) | 🇸🇦 [العربية](./README_ar.md)
</div>

---

# 🧠 PentaGo

**PentaGo** ist eine inoffizielle Python-Bibliothek zur asynchronen Nutzung der **Papago-Weboberfläche von NAVER**.  
Für den Zugriff auf die Übersetzungsfunktionen ist kein API-Schlüssel erforderlich.

> ✅ **Läuft stabil im Jahr 2025**

---

## 🚀 Merkmale

- ✅ Inoffizieller Papago-API-Wrapper
- ⚡ Unterstützt `async/await`
- 🌍 16 unterstützte Sprachen
- 💬 Ausgabe von Aussprache und Wörterbuchdaten
- 🙇 Optionaler Honorifikationsmodus

---

## 📦 Installation

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 Beispiel

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, GERMAN)
    result = await pentago.translate("PentaGo ist die beste inoffizielle Papago-API im Jahr 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 Unterstützte Sprachen

| Code   | Sprache      | Code   | Sprache      |
|--------|--------------|--------|--------------|
| `ko`   | Koreanisch   | `en`   | Englisch     |
| `ja`   | Japanisch    | `es`   | Spanisch     |
| `fr`   | Französisch  | `vi`   | Vietnamesisch|
| `th`   | Thailändisch | `id`   | Indonesisch  |
| `de`   | Deutsch      | `ru`   | Russisch     |
| `pt`   | Portugiesisch| `it`   | Italienisch  |
| `hi`   | Hindi        | `ar`   | Arabisch     |
| `auto` | Automatisch erkennen |        |      |

---

## 📄 Lizenz

Dieses Projekt steht unter der [GPL-3.0-Lizenz](LICENSE).

---

## 🤝 Mitwirken

Pull Requests, Fehlerberichte und Vorschläge sind jederzeit willkommen.
