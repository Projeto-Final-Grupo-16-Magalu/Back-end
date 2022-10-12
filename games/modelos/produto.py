from pydantic import BaseModel, Field
from typing import List, Optional


# Padrão para cadastro de produtos
class Produto(BaseModel):
    # Nome do produto
    nome: str = Field(unique=True, max_length=50)
    # Breve descrição sobre o produto
    descricao: str = Field(max_length=100)
    # Informa se é um console, periférico ou videogame
    tipo: str = Field(max_length=20)
    # Informa qual fabricante atende (Nintendo, Sony, Microsoft etc.)
    plataforma: str = Field(max_length=20)
    preco: float = Field(gt = 0.01)
    quantidade_em_estoque: int = Field(gt = 0)
    codigo: int = Field(unique=True)
    # Dados para futuras features
    imagem: str


# Dados para futuras features
class Plataforma(BaseModel):
    marca: str = Field(max_length=20)
    Produtos: List[Produto] = []


class ErroNomeJaCadastrado(BaseModel):
    """Já existe um produto cadastrado com esse nome"""
    mensagem: str


class AtualizacaoProduto(BaseModel):
    nome: Optional[str] = Field(unique=True,min_length=1, max_length=50)
    descricao: Optional [str] = Field(max_length=100)
    plataforma: Optional [str] = Field(max_length=20)
    preco: Optional[float] = Field(gt=0.01) #meninas, esse gt é o mesmo que maior >
    quantidade_em_estoque: Optional[int] = Field (gt=0)
    imagem: Optional [str]