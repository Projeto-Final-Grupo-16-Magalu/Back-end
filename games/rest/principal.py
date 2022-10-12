from fastapi import APIRouter


rota_principal = APIRouter(
    prefix=''
)


@rota_principal.get('/')
def dizer_ola():
    return 'Oi'