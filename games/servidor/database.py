from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = environ.get('DATABASE_URI')
    colecao_clientes = None
    colecao_enderecos = None
    colecao_produtos = None
    colecao_ordens_compra = None
    colecao_itens_compra = None

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
    db.colecao_clientes = db.client.carrinho_compras.clientes
    db.colecao_enderecos = db.client.carrinho_compras.enderecos
    db.colecao_produtos = db.client.carrinho_compras.produtos
    db.colecao_ordens_compra = db.client.carrinho_compras.ordens
    db.colecao_itens_compra = db.client.carrinho_compras.itens_compra

async def disconnect_db():
    db.client.close()
