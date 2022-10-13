from bson import ObjectId
from typing import Optional

from games.modelos.produto import AtualizacaoProduto
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_PRODUTOS
from games.logs import logger

colecao = obter_colecao(COLECAO_PRODUTOS)

# Cadastrar um produto
async def inserir_novo_produto(produto: dict) -> dict: 
   try:
        produto = await colecao.insert_one(produto)
        logger.info(produto)
        return produto
    except Exception as e:
        logger.exception(e)


# Atualizar os dados de um produto.
async def atualizar_por_codigo(id : str, produto: AtualizacaoProduto) ->bool:
    try:    
        logger.info(f'atualizacao={produto}')
        produto = {k: v for k, v in produto.dict().items() if v is not None}
        logger.info(produto)
        filtro = {
            '_id': ObjectId(id)
        }
        
        atualizacao = {
            "$set": produto
        }
        operacao_atualizacao = await colecao.update_one(filtro, atualizacao)
        logger.info(operacao_atualizacao)
        if operacao_atualizacao.modified_count > 0:
            produto_atualizado = await pesquisar_pelo_id(id, {'_id': 0}) 
            logger.info(produto_atualizado)
            return produto_atualizado  

        return None
    except Exception as e:
        logger.exception(e)
        
async def atualiza_produto(codigo: int, quantidade_comprada: int):
    try:
        logger.info(f'codigo={codigo} : quantidade_comprada={quantidade_comprada}')
        filtro = {
            'codigo': codigo
        }
        produto = pesquisar_pelo_codigo(codigo)
        logger.info(produto)
        novo_valor = produto['quantidade_em_estoque'] - quantidade_comprada
        logger.info(novo_valor)
        atualizacao = {'$set': {'quantidade_em_estoque': novo_valor}}
        logger.info(atualizacao)
        operacao_atualizacao = await colecao.update_one(filtro, atualizacao)
        logger.info(operacao_atualizacao)
        
        if operacao_atualizacao.modified_count > 0:
            produto_atualizado = await pesquisar_pelo_codigo(codigo)
            logger.info(produto_atualizado)
            return produto_atualizado

        return produto
    except Exception as e:
        logger.exception(e)

# Pesquisar um produto.
async def pesquisar_pelo_id(id):
    try:    
        filtro = {
            '_id' : ObjectId(id)
        }
        produto = await colecao.find_one(filtro)
        logger.info(produto)
        return produto
    except Exception as e:
        logger.exception(e)
    
        
async def pesquisar_pelo_codigo(codigo: int) -> Optional[dict]:
    try:
        filtro = {
            'codigo': codigo
        }
        produto_pesquisado = await colecao.find_one(filtro)
        logger.info(produto_pesquisado)
        return produto_pesquisado
    except Exception as e:
        logger.exception(e)
        
# Pesquisar um produto pelo nome.
async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    try:
        filtro = {
            'nome': nome
        }
        produto = await colecao.find_one(filtro)
        logger.info(produto)
        return produto
    except Exception as e:
        logger.exception(e)

# 5.Remover um produto.
# TODO: é necessário validar se existe o item em carrinhos abertos, remover e atualizar os dados do carrinho.
# Não é trivial
async def delete_produto(id):
    try:
        filtro = {
            '_id' : ObjectId(id)
        }
        remover = await colecao.delete_one(filtro)
        logger.info(remover)
        return remover
    except Exception as e:
        logger.exception(e)
