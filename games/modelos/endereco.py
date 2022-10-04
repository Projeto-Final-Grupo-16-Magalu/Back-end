from pydantic import BaseModel, Field
from typing import List

from .cliente import Cliente

class Endereco(BaseModel):
    id_cliente: int = Field(unique=True, max_digits=3)
    nome: str = Field(max_length=10)
    logradouro: str= Field(max_length=100)
    cep: str= Field(max_length=9)
    bairro: str= Field(max_length=20)
    cidade: str= Field(max_length=20)
    estado: str= Field(max_length=2)
    entrega: bool = Field(default=True)


class EnderecosCliente(BaseModel):
    cliente: Cliente
    enderecos: List[Endereco] = []

