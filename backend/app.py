from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Inventory System API", version="1.0")

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
    return {"message": "🚀 Inventory System API with Database is running!"}

# Crear producto
@app.post("/products/", response_model=schemas.ProductResponse)
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
