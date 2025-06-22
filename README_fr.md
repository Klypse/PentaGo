<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="Logo de PentaGo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+API+Papago+Asynchrone+Non+Officielle" alt="Titre animé PentaGo" />

📘 [한국어](./README.md) | 🌍 [English](./README_en.md) | 🇯🇵 [日本語](./README_ja.md) | 🇫🇷 [Français](./README_fr.md) | 🇩🇪 [Deutsch](./README_de.md) | 🇻🇳 [Tiếng Việt](./README_vi.md) | 🇸🇦 [العربية](./README_ar.md)

</div>

---

# 🧠 PentaGo

**PentaGo** est une bibliothèque Python non officielle permettant d’utiliser **l’interface web de Papago (NAVER)** de façon asynchrone.  
Aucune clé d’API n’est nécessaire pour accéder aux fonctions de traduction.

> ✅ **Fonctionne parfaitement en 2025**

---

## 🚀 Caractéristiques

- ✅ Wrapper non officiel pour Papago
- ⚡ Support natif de `async/await`
- 🌍 Prise en charge de 16 langues
- 💬 Affiche la prononciation et les résultats du dictionnaire
- 🙇 Mode honorifique activable

---

## 📦 Installation

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 Exemple d’utilisation

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, FRENCH)
    result = await pentago.translate("PentaGo est la meilleure API Papago non officielle en 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 Langues prises en charge

| Code   | Langue       | Code   | Langue       |
|--------|--------------|--------|--------------|
| `ko`   | Coréen       | `en`   | Anglais      |
| `ja`   | Japonais     | `es`   | Espagnol     |
| `fr`   | Français     | `vi`   | Vietnamien   |
| `th`   | Thaï         | `id`   | Indonésien   |
| `de`   | Allemand     | `ru`   | Russe        |
| `pt`   | Portugais    | `it`   | Italien      |
| `hi`   | Hindi        | `ar`   | Arabe        |
| `auto` | Détection automatique |        |        |

---

## 📄 Licence

Ce projet est distribué sous licence [MIT](LICENSE).

---

## 🤝 Contributions

- Pull requests et issues bienvenus !
- Suggestions, traductions ou améliorations sont encouragées.
