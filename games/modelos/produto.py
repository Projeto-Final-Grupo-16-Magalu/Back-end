from decimal import Decimal
from pydantic import BaseModel, Field, PositiveInt
from typing import List


class Produto(BaseModel):
    nome: str = Field(unique=True, max_length=50)
    descricao: str = Field(max_length=100)
    plataforma: str = Field(max_length=20)
    preco: Decimal = Field(max_digits=10, decimal_places=3)
    qantidade_em_estoque: int = Field(PositiveInt)
    codigo: int = Field(unique=True)


class Plataforma(BaseModel):
    marca: str = Field(max_length=20)
    Produtos: List[Produto] = []