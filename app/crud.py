from sqlalchemy.orm import Session
from app.models import Produto

def criar_produto(db: Session, nome: str, preco: int):
    produto = Produto(nome=nome, preco=preco)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def listar_produtos(db: Session):
    return db.query(Produto).all()

def deletar_produto(db: Session, produto_id: int):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()