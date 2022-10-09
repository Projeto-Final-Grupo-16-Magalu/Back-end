import datetime
from typing import List
from decimal import Decimal
from pydantic import BaseModel, Field, PositiveInt
from pydantic.networks import EmailStr

#from games.modelos.endereco import Endereco
from games.modelos.produto import Produto


class ItemCarrinho(BaseModel):
    produto: Produto
    quantidade: int = Field(PositiveInt)
    valor: Decimal = Field(max_digits=10, decimal_places=2)


class Carrinho(BaseModel):
    cliente: EmailStr
    quantidade_produtos: int = Field(default=0)
    valor_total: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    aberto: bool = Field(default=True)
    produtos: List = []
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    #entrega: Endereco
