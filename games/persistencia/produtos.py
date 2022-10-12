from bson import ObjectId
from typing import Optional

from games.modelos.produto import AtualizacaoProduto
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_PRODUTOS
from games.logs import logger

colecao = obter_colecao(COLECAO_PRODUTOS)

# 1.Cadastrar um produto
async def inserir_novo_produto(produto: dict) -> dict: 
    await colecao.insert_one(produto)
    logger.info(f'produto={produto}')
    return produto


# 2.Atualizar os dados de um produto.
async def atualizar_por_codigo(id : str, produto: AtualizacaoProduto) ->bool:
    logger.info(f'atualizacao={produto}')
    produto = {k: v for k, v in produto.dict().items() if v is not None}
    
    filtro = {
        '_id': ObjectId(id)
    }
    
    atualizacao = {
        "$set": produto
    }
    operacao_atualizacao = await colecao.update_one(filtro, atualizacao)
    
    if operacao_atualizacao.modified_count > 0:
        produto_atualizado = await pesquisar_pelo_id(id) 
        logger.info(f'produto_atualizado={produto_atualizado}')
        return produto_atualizado  

    return None

async def atualiza_produto(codigo: int, quantidade_comprada: int):
    logger.info(f'codigo={codigo} : quantidade_comprada={quantidade_comprada}')
    filtro = {
         'codigo': codigo
    }
    produto = pesquisar_pelo_codigo(codigo)
    novo_valor = produto['quantidade_em_estoque'] - quantidade_comprada
    atualizacao = {'$set': {'quantidade_em_estoque': novo_valor}}
    operacao_atualizacao = await colecao.update_one(filtro, atualizacao)
 
    if operacao_atualizacao.modified_count > 0:
        produto_atualizado = await pesquisar_pelo_codigo(codigo)
        logger.info(f'produto_atualizado={produto_atualizado}')
        return produto_atualizado

    return produto

# 3.Pesquisar um produto.
async def pesquisar_pelo_id(id):
    filtro = {
        '_id' : ObjectId(id)
    }
    produto = await colecao.find_one(filtro, {'_id': 0})
    return produto

async def pesquisar_pelo_codigo(codigo: int) -> Optional[dict]:
    filtro = {
        'codigo': codigo
    }
    produto_pesquisado = await colecao.find_one(filtro, {'_id': 0})
    return produto_pesquisado

# 4.Pesquisar um produto pelo nome.
async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        'nome': nome
    }
    produto = await colecao.find_one(filtro, {'_id': 0})
    return produto

# 5.Remover um produto.
# TODO: é necessário validar se existe o item em carrinhos abertos, remover e atualizar os dados do carrinho.
# Não é trivial
async def delete_produto(id):
    filtro = {
        '_id' : ObjectId(id)
    }
    remover = await colecao.delete_one(filtro)
    return remover
