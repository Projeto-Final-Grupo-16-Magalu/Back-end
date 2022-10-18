from fastapi import APIRouter, status
from games.rest.documentacao import DESCRICAO_PRINCIPAL

rota_principal = APIRouter(
    prefix=""
)

@rota_principal.get(
    "/",
    summary= "Verificação do funcionamento da API",
    description= DESCRICAO_PRINCIPAL,
    status_code=status.HTTP_200_OK, 
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "A API não está funcionando"
        }
    }
)
def dizer_ola():
    return "Oi"