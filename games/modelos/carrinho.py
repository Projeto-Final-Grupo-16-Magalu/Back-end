import datetime
from typing import List
from decimal import Decimal
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco

#Modelo para ItemCarrinho
class ItemCarrinho(BaseModel):
    produto: int
    quantidade: int
    valor: Decimal = Field(max_digits=10, decimal_places=2)

#Modelo para Carrinho
class Carrinho(BaseModel):
    cliente: EmailStr
    quantidade_produtos: int = Field(default=0)
    valor_total: float = Field(default=0)
    aberto: bool = Field(default=True)
    produtos: List[ItemCarrinho] = []
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    entrega: Endereco = Field(default=None)

#Modelo para Abrir Carrinho
class AbrirCarrinho(BaseModel):
    cliente: EmailStr

#Modelo para erro: não foi possível criar o carrinho
class ErroCarrinhoNaoCriado(BaseModel):
    """Não foi possível criar um carrinho"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foi possível criar um carrinho"
            }
        }
    
#Modelo para erro: Carrinho já criado para esse cliente
class ErroCarrinhoJaCriado(BaseModel):
    """Já existe um carrinho para esse cliente"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Já existe um carrinho para esse cliente"
            }
        }
        
#Modelo para erro: produto não cadastrado
class ErroProdutoNaoEncontrado(BaseModel):
    """Não foi possível encontrar o produto"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foi possível encontrar o produto"
            }
        }
        
#Modelo para erro: produto removido
class ErroProdutoNaoDisponivel(BaseModel):
    """O produto não está mais disponível"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "O produto não está mais disponível"
            }
        }
        
#Modelo para erro: não foi possível fechar o carrinho
class ErroCarrinhoNaoFechado(BaseModel):
    """Não foi possível fechar o carrinho"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foi possível fechar o carrinho"
            }
        }
        
#Modelo para erro: Não foi possível remover o carrinho
class ErroCarrinhoNaoRemovido(BaseModel):
    """Não foi possível remover o carrinho"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foi possível remover o carrinho"
            }
        }

#Modelo para erro: Não foi possível remover o carrinho
class ErroCarrinhoJaRemovido(BaseModel):
    """O carrinho já foi removido"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "O carrinho já foi removido"
            }
        }

#Modelo para erro: Não foi possível remover o carrinho
class ErroCarrinhosFechadosNaoExistem(BaseModel):
    """Não foram encontrados carrinhos fecahdos para esse cliente"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foram encontrados carrinhos fecahdos para esse cliente"
            }
        }       
        