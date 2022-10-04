import datetime
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List

from .cliente import Cliente
from .endereco import Endereco
from .produto import Produto


class ItemsCarrinho(BaseModel):
    cliente: Cliente
    produtos: List[Produto] = []


class Carrinho(BaseModel):
    cliente: Cliente
    produtos: List[ItemsCarrinho] = []
    preco: Decimal = Field(max_digits=10, decimal_places=2)
    pagamento: bool = Field(default=False)
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    entrega: Endereco