from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    #database_uri = environ.get('BD_URL')
    database_uri = "mongodb+srv://games:games@cluster0.udqxomv.mongodb.net"
    colecao_usuarios = None
    colecao_enderecos = None
    colecao_produtos = None
    colecao_pedidos = None
    colecao_itens_do_pedido = None


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
    db.colecao_usuarios = db.client.games.usuarios
    db.colecao_enderecos = db.client.games.enderecos
    db.colecao_produtos = db.client.games.produtos
    db.colecao_pedidos = db.client.games.pedidos
    db.colecao_itens_do_pedido = db.client.games.itens_do_pedido

async def disconnect_db():
    db.client.close()
