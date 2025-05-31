<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

📘 [韓国語](./README.md) | 🌍 [英語](./README_en.md) | 🇯🇵 [日本語](./README_ja.md)

</div>

---

# 🧠 PentaGo

**PentaGo** は NAVER パパゴのウェブインターフェースを非同期で操作する **非公式 Python 翻訳ライブラリ** です。  
API キーなしで、高品質な翻訳を簡単に行えます。

> ✅ **2025年現在も正常動作確認済み**

---

## 🚀 特徴

- ✅ **非公式 Papago API ラッパー**
- ⚡ **非同期処理 (`async/await`) 対応**
- 🌍 **16言語に対応**
- 💬 **発音・辞書情報の取得**
- 🙇 **敬語モードの使用可**

---

## 📦 インストール

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 使用例

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate("2025年最高の非公式パパゴAPIはPentaGoです。", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 対応言語

| コード | 言語             | コード | 言語             |
|--------|------------------|--------|------------------|
| `ko`   | 韓国語           | `en`   | 英語             |
| `ja`   | 日本語           | `zh-CN`| 中国語（簡体字） |
| `zh-TW`| 中国語（繁体字） | `es`   | スペイン語       |
| `fr`   | フランス語       | `vi`   | ベトナム語       |
| `th`   | タイ語           | `id`   | インドネシア語   |
| `de`   | ドイツ語         | `ru`   | ロシア語         |
| `pt`   | ポルトガル語     | `it`   | イタリア語       |
| `hi`   | ヒンディー語     | `ar`   | アラビア語       |
| `auto` | 自動判別         |        |                  |

---

## 📄 ライセンス

このプロジェクトは [GPL-3.0 ライセンス](LICENSE) のもとに公開されています。

---

## 🤝 コントリビュート

Issue や PR をいつでも歓迎しています。
