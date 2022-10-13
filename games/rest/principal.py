from fastapi import APIRouter
from fastapi.responses import FileResponse


rota_principal = APIRouter(
    prefix='',
    tags = ['Sejam bem-vindos ao Magalu Games!']
)


@rota_principal.get('/')
def dizer_ola():
    return 'Oi'


@rota_principal.get(
    '/bem_vindos')
def magalu_games():
    return FileResponse('extras/luizagamerreadme.gif')