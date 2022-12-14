from typing import List, Optional
from pydantic.networks import EmailStr

from games.configuracoes import COLECAO_CLIENTES
from games.logs import logger
from games.servidor.database import obter_colecao

import games.persistencia.enderecos as persistencia_enderecos


colecao = obter_colecao(COLECAO_CLIENTES)


async def pesquisar_pelo_email(email: EmailStr, return_id: bool = True) -> Optional[dict]:
    filtro = {
        'email': email
    }
    if return_id:
        cliente = await colecao.find_one(filtro)
    else:
        cliente = await colecao.find_one(filtro, {'_id': 0}) 
    logger.info(cliente)
    return cliente


async def pesquisar_pelo_id(id_cliente) -> Optional[dict]:
    filtro = {
        '_id': id_cliente
    }
    cliente = await colecao.find_one(filtro, {'_id': 0} )
    logger.info(cliente)
    return cliente


async def pesquisar_clientes() -> List[dict]:
    filtro = {}
    cursor_pesquisa = colecao.find(filtro,  {'_id': 0})
    lista_todos = [
        clientes
        async for clientes in cursor_pesquisa
    ]
    logger.info(lista_todos)
    return lista_todos


async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        'nome': nome
    }
    cliente = await colecao.find_one(filtro)
    logger.info(cliente)
    return cliente


async def inserir_um_novo_cliente(novo_cliente: dict) -> dict:
    resultado_insercao = await colecao.insert_one(novo_cliente)
    if resultado_insercao.acknowledged:
        cliente = await pesquisar_pelo_id(resultado_insercao.inserted_id)
        # Cria um documento na coleção ENDERECOS_CLIENTE com lista de endereços vazia
        await persistencia_enderecos.cadastrar_documento_cliente(novo_cliente['email'])
        return cliente
    return None