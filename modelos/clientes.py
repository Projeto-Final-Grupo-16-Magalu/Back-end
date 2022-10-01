from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class Cliente(BaseModel):
    email: EmailStr = Field(unique=True, index=True)
    nome: str = Field(...)
    cpf: str = Field(...)
    

    class Config:
        schema_extra = {
            "example": {
                "email": "camila.cangussu@gmail.com",
                "nome": "Camila Cangussu",
                "cpf": "08449153603"
            }
        }    