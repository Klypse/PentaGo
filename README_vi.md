<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="Biểu tượng PentaGo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+API+Papago+không+chính+thức+với+Async" alt="Dòng giới thiệu PentaGo" />

📘 [Tiếng Hàn](./README.md) | 🌍 [Tiếng Anh](./README_en.md) | 🇯🇵 [Tiếng Nhật](./README_ja.md) | 🇫🇷 [Tiếng Pháp](./README_fr.md) | 🇩🇪 [Tiếng Đức](./README_de.md) | 🇻🇳 [Tiếng Việt](./README_vi.md) | 🇸🇦 [Tiếng Ả Rập](./README_ar.md)
</div>

---

# 🧠 PentaGo

**PentaGo** là thư viện Python không chính thức sử dụng **giao diện web Papago của NAVER** theo cách bất đồng bộ.  
Không cần khoá API — vẫn sử dụng được toàn bộ chức năng dịch.

> ✅ **Đã xác nhận hoạt động tốt năm 2025**

---

## 🚀 Tính năng

- ✅ API Papago không chính thức
- ⚡ Hỗ trợ `async/await`
- 🌍 Hỗ trợ 16 ngôn ngữ
- 💬 Trả về phát âm và kết quả từ điển
- 🙇 Có tùy chọn chế độ kính ngữ

---

## 📦 Cài đặt

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

---

## 🧪 Ví dụ sử dụng

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, VIETNAMESE)
    result = await pentago.translate("PentaGo là API Papago không chính thức tốt nhất năm 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 Ngôn ngữ được hỗ trợ

| Mã    | Ngôn ngữ      | Mã    | Ngôn ngữ       |
|-------|---------------|-------|----------------|
| `ko`  | Tiếng Hàn     | `en`  | Tiếng Anh      |
| `ja`  | Tiếng Nhật    | `es`  | Tiếng Tây Ban Nha |
| `fr`  | Tiếng Pháp    | `vi`  | Tiếng Việt     |
| `th`  | Tiếng Thái    | `id`  | Tiếng Indonesia|
| `de`  | Tiếng Đức     | `ru`  | Tiếng Nga      |
| `pt`  | Tiếng Bồ Đào Nha | `it` | Tiếng Ý     |
| `hi`  | Tiếng Hindi   | `ar`  | Tiếng Ả Rập    |
| `auto`| Phát hiện tự động |     |                |

---

## 📄 Giấy phép

Dự án này sử dụng giấy phép [GPL-3.0](LICENSE).

---

## 🤝 Góp phần

Luôn hoan nghênh pull request, issue và đóng góp từ cộng đồng.
