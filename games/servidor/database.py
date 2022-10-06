from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    #database_uri = environ.get('BD_URL')
    database_uri = "mongodb+srv://games:games@cluster0.udqxomv.mongodb.net"
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
    db.colecao_clientes = db.client.games.clientes
    db.colecao_enderecos = db.client.games.enderecos
    db.colecao_produtos = db.client.games.produtos
    db.colecao_carrinhos = db.client.games.carrinhos

async def disconnect_db():
    db.client.close()
