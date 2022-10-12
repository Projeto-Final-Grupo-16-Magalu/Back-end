import datetime
from typing import List
from decimal import Decimal
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco


class ItemCarrinho(BaseModel):
    produto: int
    quantidade: int
    valor: Decimal = Field(max_digits=10, decimal_places=2)


class Carrinho(BaseModel):
    cliente: EmailStr
    quantidade_produtos: int = Field(default=0)
    valor_total: float = Field(default=0)
    aberto: bool = Field(default=True)
    produtos: List[ItemCarrinho] = []
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    entrega: Endereco = Field(default=None)


class AbrirCarrinho(BaseModel):
    cliente: EmailStr
