# Portafolio Avanzado

Este proyecto es una versión más robusta de mi portafolio en HTML, CSS y JavaScript, con un backend FastAPI básico para el formulario de contacto.

## Estructura
- `index.html`: Página principal
- `style/`: Archivos de estilos
- `js/`: Funciones y scripts
- `backend/`: API con FastAPI (productos y contacto)
- `assets/`: Imágenes y recursos

## Cómo usar
- Frontend: abre `index.html` en tu navegador.
- Backend: ejecuta `uvicorn backend.app:app --reload` y asegúrate de tener las dependencias instaladas (`pip install -r requirements.txt`).

El formulario de contacto envía datos a `http://127.0.0.1:8000/contacto/`.
