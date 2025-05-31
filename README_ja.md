<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

</div>

---

# 🧠 PentaGo

**PentaGo** は、**NAVER パパゴのウェブインターフェース**を非同期で操作できる **非公式 Python 翻訳ライブラリ**です。  
API キー不要で、パパゴと同等の翻訳機能を簡単に利用できます。

> ✅ **2025年現在も正常に動作しています。**  
> 最新のパパゴウェブ構造に合わせてメンテナンスされています。

---

## 🚀 特徴

- ✅ **非公式パパゴAPIラッパー**
- ⚡ **非同期処理対応 (`async/await`)**
- 🌍 **16言語に対応**
- 💬 **発音・辞書情報も取得可能**
- 🙇 **敬語（honorific）モード対応**

---

## 📦 インストール方法

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

> 本プロジェクトは PyPI には公開されていません。リポジトリを直接クローンしてご利用ください。

---

## 🧪 使用例

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate(\"2025年最高の非公式パパゴAPIはPentaGoです。\", honorific=True)
    print(result)

if __name__ == \"__main__\":
    asyncio.run(main())
```

### 出力例:
```json
{
  "source": "ja",
  "target": "en",
  "text": "2025年最高の非公式パパゴAPIはPentaGoです。",
  "translatedText": "The best unofficial Papago API in 2025 is PentaGo.",
  "sound": "za besuto anofisharu papago ēpīai in nisen nijūgo wa pentago desu",
  "srcSound": "nisen nijūgonen saikō no hikōshiki papago api wa pentago desu"
}
```

---

## 🌐 対応言語

| コード | 言語         | コード | 言語         |
|--------|--------------|--------|--------------|
| ko     | 韓国語       | en     | 英語         |
| ja     | 日本語       | zh-CN  | 中国語（簡体）|
| zh-TW  | 中国語（繁体）| es     | スペイン語   |
| fr     | フランス語   | vi     | ベトナム語   |
| th     | タイ語       | id     | インドネシア語 |
| de     | ドイツ語     | ru     | ロシア語     |
| pt     | ポルトガル語 | it     | イタリア語   |
| hi     | ヒンディー語 | auto   | 自動判別     |

---

## 📁 プロジェクト構成

```
PentaGo/
├── pentago/
│   ├── __init__.py
│   ├── main.py        # 非同期ロジックの本体
│   └── lang.py        # 言語コード定義
└── examples/
    └── basic.py       # サンプルコード
```

---

## 📄 ライセンス

このプロジェクトは [GPL-3.0 ライセンス](LICENSE) のもとで提供されています。

---

## 🤝 コントリビュート歓迎

- Issue や Pull Request はいつでも歓迎します！
- 機能追加・バグ修正・改善など、ぜひご参加ください。

---

<div align="center">

💡 _PentaGo は、API キー不要でパパゴの力を最大限に引き出せる非公式ツールです。_  
🌐 _軽量・高速・柔軟。すべての開発者へ。_

</div>
