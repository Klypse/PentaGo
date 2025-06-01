<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="شعار PentaGo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+واجهة+برمجة+تطبيقات+Papago+غير+رسمية+باستخدام+Async" alt="عنوان PentaGo" />

📘 [الكورية](./README.md) | 🌍 [الإنجليزية](./README_en.md) | 🇯🇵 [اليابانية](./README_ja.md) | 🇫🇷 [الفرنسية](./README_fr.md) | 🇩🇪 [الألمانية](./README_de.md) | 🇻🇳 [الفيتنامية](./README_vi.md) | 🇸🇦 [العربية](./README_ar.md)

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
