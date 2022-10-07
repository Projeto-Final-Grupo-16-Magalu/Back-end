from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = environ.get('DATABASE_URI')
    colecao_clientes = None
    colecao_enderecos = None
    colecao_produtos = None
    colecao_carrinhos = None

db = DataBase()

async def connect_db():
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
# async def acessar_colecao (db.client):
#     ...
    
    db.colecao_clientes = db.client.magalugames.clientes
    db.colecao_enderecos = db.client.magalugames.enderecos
    db.colecao_produtos = db.client.magalugames.produtos
    db.colecao_carrinhos = db.client.magalugames.carrinhos

async def disconnect_db():
    db.client.close()
