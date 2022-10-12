from decimal import Decimal
from operator import gt
from pydantic import BaseModel, Field, PositiveInt
from typing import List, Optional
from bson import ObjectId

class Produto(BaseModel):
    nome: str = Field(unique=True, max_length=50)
    descricao: str = Field(max_length=100)
    plataforma: str = Field(max_length=20)
    preco: float = Field(gt = 0.01)
    quantidade_em_estoque: int = Field(gt = 0)
    codigo: Optional[int] = Field(unique=True)
    imagem: str

class Plataforma(BaseModel):
    marca: str = Field(max_length=20)
    Produtos: List[Produto] = []

class ErroNomeJaCadastrado(BaseModel):
    """Já existe um produto cadastrado com esse nome"""
    mensagem: str





#testando
class AtualizacaoProduto(BaseModel):
    nome: Optional[str] = Field(unique=True,min_length=1, max_length=50)
    descricao: Optional [str] = Field(max_length=100)
    plataforma: Optional [str] = Field(max_length=20)
    preco: Optional[float] = Field(gt=0.01) #meninas, esse gt é o mesmo que maior > 
    quantidade_em_estoque: Optional[int] = Field (gt=0)
    imagem: Optional [str]