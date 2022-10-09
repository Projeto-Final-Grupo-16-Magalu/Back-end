from decimal import Decimal
from pydantic import BaseModel, Field, PositiveInt
from typing import List, Optional


class Produto(BaseModel):
    nome: str = Field(unique=True, max_length=50)
    descricao: str = Field(max_length=100)
    plataforma: str = Field(max_length=20)
    preco: float
    quantidade_em_estoque: int
    codigo: Optional[int] = Field(unique=True)
    imagem: str

class Plataforma(BaseModel):
    marca: str = Field(max_length=20)
    Produtos: List[Produto] = []

class ErroNomeJaCadastrado(BaseModel):
    """Já existe um produto cadastrado com esse nome"""
    mensagem: str