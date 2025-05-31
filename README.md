<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

📘 [한국어](./README.md) | 🌍 [English](./README_en.md) | 🇯🇵 [日本語](./README_ja.md)

</div>

---

# 🧠 PentaGo

**PentaGo**는 네이버 파파고 웹 인터페이스를 비동기로 사용하는 **비공식 Python 번역 라이브러리**입니다.  
공식 API 키 없이도 간편하게 고성능 번역을 구현할 수 있습니다.

> ✅ **2025년에도 정상 작동 중입니다.**

---

## 🚀 특징

- ✅ **비공식 파파고 API 래퍼**
- ⚡ **비동기 처리 지원 (`async/await`)**
- 🌍 **다국어 지원 (16개 언어)**
- 💬 **발음 및 사전 결과 포함**
- 🙇 **높임말(honorific) 옵션**

---

## 📦 설치 방법

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 사용 예시

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate("2025년 최고의 파파고 비공식 API는 PentaGo입니다.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 지원 언어

| 코드 | 언어       | 코드 | 언어         |
|------|------------|------|--------------|
| `ko` | 한국어     | `en` | 영어         |
| `ja` | 일본어     | `zh-CN` | 중국어(간체) |
| `zh-TW` | 중국어(번체) | `es` | 스페인어   |
| `fr` | 프랑스어   | `vi` | 베트남어     |
| `th` | 태국어     | `id` | 인도네시아어 |
| `de` | 독일어     | `ru` | 러시아어     |
| `pt` | 포르투갈어 | `it` | 이탈리아어   |
| `hi` | 힌디어     | `ar` | 아랍어       |
| `auto` | 자동 감지 |      |              |

---

## 📄 라이선스

이 프로젝트는 [GPL-3.0 라이선스](LICENSE)를 따릅니다.

---

## 🤝 기여

Issue 또는 PR은 언제든지 환영합니다.
