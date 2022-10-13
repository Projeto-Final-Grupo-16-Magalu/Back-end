from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from typing import Optional

#Modelo para Cleinte
class Cliente(BaseModel):
    nome: str = Field(max_length=50)
    email: EmailStr 
    senha: str = Field(min_length=4, max_length=20)
    cliente_ativo: Optional[bool] = Field(default=True)
    administrador: Optional[bool] = Field(default=False)
    
#Modelo para erro: email já cadastrado
class ErroEmailJaCadastrado(BaseModel):
    """Já existe um cliente cadastrado com esse email informado"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Já existe um cliente cadastrado com esse email"
            }
        }

#Modelo para erro: cliente não encontrado
class ErroClienteNaoEncontrado(BaseModel):
    """Não foi encontrado nenhum cadasto em nosso Banco de Dados"""
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do erro"
    )
    class Config:
        schema_extra={
            "example": {
                "mensagem": "Não foi encontrado nenhum cadasto em nosso Banco de Dados"
            }
        }
    