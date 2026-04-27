from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtos")
def criar(nome: str, preco: int, db: Session = Depends(get_db)):
    return crud.criar_produto(db, nome, preco)

@app.get("/produtos")
def listar(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

@app.delete("/produtos/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    crud.deletar_produto(db, id)
    return {"msg": "Deletado"}