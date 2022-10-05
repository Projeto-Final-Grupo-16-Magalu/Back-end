from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from typing import Optional


class Cliente(BaseModel):
    nome: str = Field(max_length=50)
    email: EmailStr = Field(unique=True, index=True, max_length=256)
    senha: str = Field(min_length=4, max_length=8)
    cliente_ativo: bool = Field(Optional, default=True)
    administrador: bool = Field(Optional, default=False)
