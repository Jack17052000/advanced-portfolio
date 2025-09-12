from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para que tu HTML (GitHub Pages) pueda hablar con FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringir a tu dominio luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contacto/")
async def contacto(
    nombre: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(""),
    mensaje: str = Form(...)
):
    # Aquí puedes guardar en DB o enviar correo
    print("Nuevo mensaje recibido:")
    print(f"Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}")

    return {"ok": True, "msg": f"¡Gracias {nombre}! Hemos recibido tu mensaje."}
