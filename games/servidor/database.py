import asyncio
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
    )


def iniciar_cliente_mongo() -> AsyncIOMotorClient:
    # Conectando no banco de dados
    cliente_mongo = AsyncIOMotorClient('mongodb+srv://games:games@cluster0.udqxomv.mongodb.net/games')
    cliente_mongo.get_io_loop = asyncio.get_event_loop
    return cliente_mongo


cliente_mongo = iniciar_cliente_mongo()


def obter_base_dados() -> AsyncIOMotorDatabase:
    # Obtém a base de dados (database) padrão
    # (a que está na string de conexão)
    return cliente_mongo.get_default_database()


def obter_colecao(nome_colecao: str) -> AsyncIOMotorCollection:
    # Obtém a coleção informada da base de dados padrão.
    bd = obter_base_dados()
    colecao = bd[nome_colecao]
    return colecao