from decimal import Decimal
from operator import gt
from pydantic import BaseModel, Field, PositiveInt
from typing import List, Optional
from bson import ObjectId

# Modelo para produto
class Produto(BaseModel):
    nome: str = Field(unique=True, max_length=50)
    descricao: str = Field(max_length=100)
    tipo: str = Field(max_length=20) #define se é console ou jogo
    plataforma: str = Field(max_length=20)
    preco: float = Field(gt = 0.01)
    quantidade_em_estoque: int = Field(gt = 0)
    codigo: Optional[int] = Field(unique=True)
    imagem: str

# Modelo para plataforma
class Plataforma(BaseModel):
    marca: str = Field(max_length=20)
    Produtos: List[Produto] = []


#Modelo para Atualização Produto
class AtualizacaoProduto(BaseModel):
    nome: Optional[str] = Field(unique=True,min_length=1, max_length=50)
    descricao: Optional [str] = Field(max_length=100)
    plataforma: Optional [str] = Field(max_length=20)
    preco: Optional[float] = Field(gt=0.01) #meninas, esse gt é o mesmo que maior > 
    quantidade_em_estoque: Optional[int] = Field (gt=0)
    imagem: Optional [str]
    
# Modelo para erro: Já exisste um produto com esse nome 
class ErroProdutoJaCadastrado(BaseModel):
    """Esse produto já foi cadastrado"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
class Config:
        schema_extra={
            "example": {
                "mensagem": "Esse produto já foi cadastrado"
            }
        }

# Modelo para erro: Já exisste um produto com esse nome 
class ErroNomeJaCadastrado(BaseModel):
    """Já existe um produto cadastrado com esse nome"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
class Config:
        schema_extra={
            "example": {
                "mensagem": "Já existe um produto cadastrado com esse nome"
            }
        }

# Modelo para erro: Já exisste um produto com esse nome 
class ErroNomeJaRemovido(BaseModel):
    """Esse produto já foi removido"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
class Config:
        schema_extra={
            "example": {
                "mensagem": "Esse produto já foi removido"
            }
        }