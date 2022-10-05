import datetime
from pydantic import BaseModel, Field, PositiveInt
from typing import List

from .cliente import Cliente
from .endereco import Endereco
from .produto import Produto


class ItemsCarrinho(BaseModel):
    produtos: Produto
    quantidade: int = Field(PositiveInt)
    valor: float = Field(max_digits=10, decimal_places=2)


class Carrinho(BaseModel):
    cliente: Cliente
    produtos: List[ItemsCarrinho] = []
    preco: float = Field(max_digits=10, decimal_places=2)
    pagamento: bool = Field(default=False)
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    entrega: Endereco