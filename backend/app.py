from fastapi import FastAPI, Depends, HTTPException, Form, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, database

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Inventory System API", version="1.0")

# CORS (permitir llamadas desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta raíz
@app.get("/")
def root():
    return {"message": "Inventory System API with Database is running!"}

# Crear producto
@app.post("/products/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.name == product.name).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    new_product = models.Product(name=product.name, stock=product.stock)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Listar productos
@app.get("/products/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# Obtener un producto por ID
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Actualizar un producto (PUT)
@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Validar nombre duplicado si cambia
    if payload.name is not None:
        other = db.query(models.Product).filter(models.Product.name == payload.name, models.Product.id != product_id).first()
        if other:
            raise HTTPException(status_code=400, detail="Product name already in use")
        product.name = payload.name

    if payload.stock is not None:
        product.stock = payload.stock

    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Eliminar un producto
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"ok": True, "message": "Product deleted"}

# Endpoint de contacto (recibe formulario)
@app.post("/contacto/")
async def contacto(
    nombre: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(""),
    mensaje: str = Form(...),
):
    # Aquí podrías guardar en DB o enviar correo
    print("Nuevo mensaje recibido:")
    print(f"Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}")

    return {"ok": True, "msg": f"¡Gracias {nombre}! Hemos recibido tu mensaje."}

