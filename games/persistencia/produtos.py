# from motor.motor_asyncio import AsyncIOMotorClient
# from games.servidor import database
# from games.servidor.database import connect_db, db, disconnect_db


# async def cria_produto(produto):
#     await connect_db()
#     colecao_produtos = db.colecao_produtos

#     try:
#         produto = await colecao_produtos.insert_one(produto)

#         #if produto.inserted_id:
#            # produto = await cria_produto(colecao_produtos, produto.inserted_id)
#         await  disconnect_db()
#         return produto.inserted_id

#     except Exception as e:
#         print(f'cria_produto.erro: {e}')


from typing import List, Optional
from games.modelos.produto import Produto
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_PRODUTOS

# async def inserir_novo_produto(produto: dict) -> dict:
#     colecao = obter_colecao(COLECAO_PRODUTOS)
#     await colecao.insert_one(produto)
#     return produto


async def pesquisar_todos_produtos()-> Optional[dict]:
    filtro = {}
    cursor_pesquisa = obter_colecao(COLECAO_PRODUTOS).find(filtro)
    lista_todos = [
        produtos
        async for produtos in cursor_pesquisa
    ]
    return lista_todos

async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        "nome" : nome
    }
    colecao = obter_colecao(COLECAO_PRODUTOS)
    produto_nome = await colecao.find_one(filtro)

    return produto_nome

async def pesquisar_pelo_codigo(codigo: int) -> Optional[dict]:
    colecao = obter_colecao(COLECAO_PRODUTOS)
    filtro = {
        'codigo': codigo
    }
    produto_pesquisado = await colecao.find_one(filtro)
    return produto_pesquisado

async def atualiza_produto(codigo: int, quantidade_comprada: int):
    colecao = obter_colecao(COLECAO_PRODUTOS)
    filtro = {
        'codigo': codigo
    }
    produto = await colecao.find_one(filtro)
    novo_valor = produto['quantidade_em_estoque'] - quantidade_comprada
    atualizacao = {'$set': {'quantidade_em_estoque': novo_valor}}
    produto_atualizado = await colecao.update_one(filtro, atualizacao)
    return produto_atualizado

