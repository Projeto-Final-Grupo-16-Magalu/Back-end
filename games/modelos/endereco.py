from pydantic import BaseModel, EmailStr, Field
from typing import List

from games.modelos.cliente import Cliente

class Endereco(BaseModel):
    nome: str = Field(max_length=10)
    logradouro: str= Field(max_length=100)
    cep: str= Field(max_length=9)
    bairro: str= Field(max_length=20)
    cidade: str= Field(max_length=20)
    estado: str= Field(max_length=2)
    numero: str= Field(max_length=10)
    entrega: bool = Field(default=True)


class EnderecosCliente(BaseModel):
    cliente: EmailStr
    enderecos: List[Endereco] = []

#Modelo para erro: endereço já cadastrado para esse usuário
class ErroEnderecoJaCadastrado(BaseModel):
    """Esse endereço já foi cadastrado para esse usuário"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Esse endereço já foi cadastrado para esse usuário"
            }
        }
