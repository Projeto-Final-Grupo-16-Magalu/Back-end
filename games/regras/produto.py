from fastapi import HTTPException

import games.persistencia.produtos as produtos_persistencia
from games.modelos.produto import AtualizacaoProduto, Produto
from games.regras.excecoes import NaoEncontradoExcecao
from games.logs import logger

# VALIDAR A CRIAÇÃO DO PRODUTO
async def inserir_novo_produto(produto: Produto) -> Produto:
    
    # Validar se o produto já existe
    await validar_produto(produto)
    produto = produto.dict()

    # Caso propduto não seja encontrado, fazer o cadastro
    novo_produto = await produtos_persistencia.inserir_novo_produto(produto)
    logger.info(f'produto={novo_produto}')

    # Retornando o registro do produto completo
    return Produto(**novo_produto)

# Validar se o produto já está cadastrado
async def validar_produto(novo_produto: Produto):
    outro_produto = await produtos_persistencia.pesquisar_pelo_nome(novo_produto.nome)
    
    # Caso o produto já tenha sido cadastrado, lança exceção
    if outro_produto is not None:
        logger.warning(f'Há outro produto com este nome={novo_produto.nome}')
        # O status de resposta 409 Conflict indica que a solicitação atual conflitou com o recurso que está no servidor.
        raise HTTPException(status_code=409, detail=f'Há outra produto com este nome')  

# Atualizar
async def atualizar_por_codigo(codigo: str, produto: AtualizacaoProduto):
        # Atualizar produto pelo código
        produto_atualizado = await produtos_persistencia.atualizar_por_codigo(codigo, produto)
        
        # Caso produto atualizado não seja encontrado, lança exceção
        if produto_atualizado == None:
            logger.warning(f'Produto não encontrado : codigo={codigo}')
            # Not found
            raise HTTPException(status_code=404, detail=f'Produto não encontrado')   
        
        logger.info(f'produto={produto_atualizado}')
        return produto_atualizado

           
# Pesquisar produto pelo ID
async def validar_id_produto(id: str):
    # Pesquisar se o produto existe pelo id produto
    produto = await produtos_persistencia.pesquisar_pelo_id(id)
    # Caso produto não existe, lança exceção
    if produto == None:
        logger.warning(f'Produto não encontrado : id={id}')
        raise NaoEncontradoExcecao("Não há  produto com este id")
    return produto

# Deletar produto pelo ID
async def delete_produto(id: str):
    # Deletar produto pelo Id
    produto_deletado = await produtos_persistencia.delete_produto(id)
    
    # Caso produto for encontrado, deletar
    if produto_deletado.deleted_count:
        return{'status': 'Produto deletado com sucesso!'}
    
    # Caso produto não existe, lança exceção
    if produto == None:
        logger.warning(f'Produto não encontrado : id={id}')
        raise NaoEncontradoExcecao("Não há  produto com este id")    
    return None