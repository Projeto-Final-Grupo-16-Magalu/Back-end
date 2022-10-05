from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from games.rest.principal import rota_principal
from games.rest.games import rota_games
from games.rest.carrinho import rota_carrinho

def configurar_rotas(app: FastAPI):
    app.include_router(rota_principal)
    app.include_router(rota_games)
    app.include_router(rota_carrinho)

############  Meninas, essa conf do Cors é para receber o front se houver tempo ##################
def configurar_api_rest(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def criar_aplicacao_fastapi():
    app = FastAPI()

    configurar_api_rest(app)
    configurar_rotas(app)

    return app