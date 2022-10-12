from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from typing import List


# Padrão para cadastro de endereço
class Endereco(BaseModel):
    # Apelido para o endereço ex.: Casa
    nome: str = Field(max_length=10)
    logradouro: str= Field(max_length=100)
    cep: str= Field(max_length=9)
    bairro: str= Field(max_length=20)
    cidade: str= Field(max_length=20)
    estado: str= Field(max_length=2)
    numero: str= Field(max_length=10)
    # Define se o endereço é o escolhido para entrega
    entrega: bool = Field(default=True)


# Padrão para banco de dados de endereços por cliente
class EnderecosCliente(BaseModel):
    # Email do cliente
    cliente: EmailStr
    # Lista dos endereços cadastrados
    enderecos: List[Endereco] = []


# Modelo para erro: endereço já cadastrado para esse usuário
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


# Modelo para erro: endereço não encontrado
class ErroEnderecoNaoEncontrado(BaseModel):
    """Esse endereço não está cadastrado"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Esse endereço não está cadastrado"
            }
        }


# Modelo para erro: endereço já removido
class ErroEnderecoJaRemovido(BaseModel):
    """Esse endereço já foi removido do sistema"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Esse endereço já foi removido do sistema"
            }
        }