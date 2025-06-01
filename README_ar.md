<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="شعار PentaGo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+%D9%88%D8%A7%D8%AC%D9%87%D8%A9+%D8%A8%D8%B1%D9%85%D8%AC%D8%A9+%D8%AA%D8%B7%D8%A8%D9%8A%D9%82%D8%A7%D8%AA+Papago+%D8%BA%D9%8A%D8%B1+%D8%B1%D8%B3%D9%85%D9%8A%D8%A9+%D8%A8%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85+Async" alt="PentaGo - واجهة Papago غير رسمية" />

📘 [한국어](./README.md) | 🌍 [English](./README_en.md) | 🇯🇵 [日本語](./README_ja.md) | 🇫🇷 [Français](./README_fr.md) | 🇩🇪 [Deutsch](./README_de.md) | 🇻🇳 [Tiếng Việt](./README_vi.md) | 🇸🇦 [العربية](./README_ar.md)

</div>

---

# 🧠 PentaGo

**PentaGo** هي مكتبة Python غير رسمية تتيح التفاعل مع واجهة Papago على الويب من خلال المعالجة غير المتزامنة.  
لا حاجة لمفتاح API — يمكنك الترجمة مباشرةً.

> ✅ **تم التحقق من عملها بشكل كامل في عام 2025**

---

## 🚀 الميزات

- ✅ واجهة Papago غير رسمية
- ⚡ دعم async/await
- 🌍 دعم 16 لغة مختلفة
- 💬 نتائج نطق ومعجم مضمنة
- 🙇 خيار الوضع الرسمي (Honorific)

---

## 📦 التثبيت

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 مثال على الاستخدام

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, ARABIC)
    result = await pentago.translate("PentaGo هي أفضل واجهة Papago غير رسمية في 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 اللغات المدعومة

| الرمز | اللغة         | الرمز | اللغة         |
|-------|----------------|-------|----------------|
| `ko`  | الكورية         | `en`  | الإنجليزية     |
| `ja`  | اليابانية       | `es`  | الإسبانية      |
| `fr`  | الفرنسية        | `vi`  | الفيتنامية     |
| `th`  | التايلاندية     | `id`  | الإندونيسية    |
| `de`  | الألمانية       | `ru`  | الروسية        |
| `pt`  | البرتغالية      | `it`  | الإيطالية      |
| `hi`  | الهندية         | `ar`  | العربية         |
| `auto` | الكشف التلقائي |       |                |

---

## 📄 الترخيص

يتم توزيع هذا المشروع بموجب ترخيص [GPL-3.0](LICENSE).

---

## 🤝 المساهمة

جميع المساهمات مرحب بها — سواء من خلال PRs أو تقارير الأخطاء أو تحسينات الأداء.
