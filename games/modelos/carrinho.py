import datetime

from decimal import Decimal
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from typing import List

from games.modelos.endereco import Endereco


# Padrão para entrada de produtos no carrinho
class ItemCarrinho(BaseModel):
    # Código do produto
    produto: int
    # Quantidade do produto no carrinho
    quantidade: int
    #Valor total do item * quantidade
    valor: Decimal = Field(max_digits=10, decimal_places=2)


# Padrão para carrinho de compras
class Carrinho(BaseModel):
    # Email do cliente
    cliente: EmailStr
    # Quantidade de produtos inseridos no carrinho
    quantidade_produtos: int = Field(default=0)
    # Valor total de todos os produtos inseridos
    valor_total: float = Field(default=0)
    # Define se o carrinho ainda está aberto para compras
    aberto: bool = Field(default=True)
    # Lista de produtos inseridos no carrinho seguindo o formato ItemCarrinho
    produtos: List[ItemCarrinho] = []
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    # Endereço para entrega
    entrega: Endereco = Field(default=None)


# Padrão para abertura de carrinho
class AbrirCarrinho(BaseModel):
    cliente: EmailStr
