<div align="center">

<img src="https://raw.githubusercontent.com/Klypse/PentaGo/main/assets/pentago-logo.png" width="180" alt="PentaGo Logo" />

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=30&duration=3000&pause=1000&color=00FFFF&center=true&vCenter=true&width=800&lines=PentaGo+-+Async+Papago+Unofficial+API" alt="Orbitron Heading" />

📘 [Coreano](./README.md) | 🌍 [Inglés](./README_en.md) | 🇯🇵 [Japonés](./README_ja.md) | 🇪🇸 [Español](./README_es.md)

</div>

---

# 🧠 PentaGo

**PentaGo** es una biblioteca de traducción en Python que interactúa de forma asíncrona con la **interfaz web de Papago (NAVER)**.  
No se requiere ninguna clave de API para acceder a todas sus funcionalidades.

> ✅ **Verificado y funcionando en 2025**

---

## 🚀 Características

- ✅ **Wrapper no oficial de la API de Papago**
- ⚡ **Soporte asincrónico (`async/await`)**
- 🌍 **Compatibilidad con 16 idiomas**
- 💬 **Incluye pronunciación y resultados de diccionario**
- 🙇 **Modo honorífico opcional**

---

## 📦 Instalación

```bash
git clone https://github.com/Klypse/PentaGo.git
cd PentaGo
```

> Esta biblioteca no está publicada en PyPI. Por favor, clónala directamente desde el repositorio.

---

## 🧪 Ejemplo de uso

```python
from pentago import Pentago
from pentago.lang import *

import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    result = await pentago.translate("PentaGo es la mejor API no oficial de Papago en 2025.", honorific=True)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 Idiomas compatibles

| Código | Idioma          | Código | Idioma          |
|--------|------------------|--------|------------------|
| `ko`   | Coreano          | `en`   | Inglés           |
| `ja`   | Japonés          | `zh-CN`| Chino simplificado |
| `zh-TW`| Chino tradicional| `es`   | Español          |
| `fr`   | Francés          | `vi`   | Vietnamita       |
| `th`   | Tailandés        | `id`   | Indonesio        |
| `de`   | Alemán           | `ru`   | Ruso             |
| `pt`   | Portugués        | `it`   | Italiano         |
| `hi`   | Hindi            | `ar`   | Árabe            |
| `auto` | Detección automática |    |                  |

---

## 📄 Licencia

Este proyecto está licenciado bajo la [licencia GPL-3.0](LICENSE).

---

## 🤝 Contribuciones

- ¡Pull requests e issues siempre son bienvenidos!
- Puedes contribuir con nuevas funciones, correcciones de errores o mejoras generales.

---

<div align="center">

💡 _PentaGo es una implementación no oficial y elegante de la API de Papago._  
🌐 _Rápido. Ligero. Sin claves de API._

</div>
