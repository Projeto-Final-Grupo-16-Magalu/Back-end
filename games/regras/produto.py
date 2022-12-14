from fastapi import HTTPException

from games.logs import logger
from games.modelos.produto import AtualizacaoProduto, Produto

import games.persistencia.produtos as produtos_persistencia


# Validar a criação de produto
async def inserir_novo_produto(produto: Produto) -> Produto:
    await validar_produto(produto)
    produto = produto.dict()
    novo_produto = await produtos_persistencia.inserir_novo_produto(produto)
    logger.info(f'produto={novo_produto}')
    # Retornando o registro do produto completo
    return Produto(**novo_produto)


async def validar_produto(novo_produto: Produto):
    outro_produto = await produtos_persistencia.pesquisar_pelo_nome(novo_produto.nome)
    if outro_produto is not None:
        logger.warning(f'Há outro produto com este nome={novo_produto.nome}')
        # O status de resposta 409 Conflict indica que a solicitação atual conflitou com o recurso que está no servidor.
        raise HTTPException(status_code=409, detail=f'Há outra produto com este nome')


# Atualizar
async def atualizar_por_codigo(codigo: str, produto: AtualizacaoProduto):
        produto_atualizado = await produtos_persistencia.atualizar_por_codigo(codigo, produto)
        if produto_atualizado == None:
            logger.warning(f'Produto não encontrado : codigo={codigo}')
            # Not found
            raise HTTPException(status_code=404, detail=f'Produto não encontrado')
        logger.info(f'produto={produto_atualizado}')
        return produto_atualizado


# Pesquisar ID
async def pesquisar_pelo_id(id: str):
    produto = await produtos_persistencia.pesquisar_pelo_id(id)
    if produto == None:
        logger.warning(f'Produto não encontrado : id={id}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Produto não encontrado')
    return produto


# Pesquisar código
async def pesquisar_pelo_codigo(codigo: int):
    produto = await produtos_persistencia.pesquisar_pelo_codigo(codigo)
    if produto == None:
        logger.warning(f'Produto não encontrado : codigo={codigo}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Produto não encontrado')
    return produto


# Pesquisar nome
async def pesquisar_pelo_nome(nome: str):
        produto = await produtos_persistencia.pesquisar_pelo_nome(nome)
        if produto == None:
            logger.warning(f'Produto não encontrado : nome={nome}')
            # Not found
            raise HTTPException(status_code=404, detail=f'Produto não encontrado')
        logger.info(f'produto={produto}')
        return produto


#Deletar
async def delete_produto(id: str):
    produto_deletado = await produtos_persistencia.delete_produto(id)
    if produto_deletado.deleted_count:
        return{'status': 'Produto deletado com sucesso!'}
    else:
        return{'status': 'Produto inexistente'}
