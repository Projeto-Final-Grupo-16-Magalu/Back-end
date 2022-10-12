from fastapi import HTTPException
from typing import List
from games.configuracoes import COLECAO_PRODUTOS
from games.modelos import produto
import games.persistencia.produtos as produtos_persistencia
from games.modelos.produto import AtualizacaoProduto, Produto
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.servidor.database import obter_colecao

# VALIDAR A CRIAÇÃO DO PRODUTO
async def inserir_novo_produto(produto: Produto) -> Produto:
    await validar_produto(produto)
    novo_produto = produto.dict()

    await produtos_persistencia.inserir_novo_produto(novo_produto)

    # Retornando o registro do produto completo
    produto_geral = Produto(**novo_produto)
    return produto_geral

async def validar_produto(novo_produto: Produto):
    
    outro_produto = await produtos_persistencia.pesquisar_pelo_nome(novo_produto.nome)
    if outro_produto is not None:
        raise HTTPException(status_code=409, detail=f'Há outra produto com este nome')  

# O status de resposta 409 Conflict indica que a solicitação atual conflitou com o recurso que está no servidor.

# ATUALIZAR
async def atualizar_por_codigo(codigo: str, produto: AtualizacaoProduto):
    
        atualizar_produto = await produtos_persistencia.atualizar_por_codigo(codigo,produto)
            
        if atualizar_produto.modified_count:
            return{'status': 'Produto atualizado com sucesso!'}
        else: 
           raise HTTPException(status_code=404, detail=f'Produto não encontrado')   
  
    

# PESQUISAR ID
async def validar_id_produto(id: str):
    id_produto = await produtos_persistencia.pesquisar_pelo_id_produto(id)
    if not id_produto:
       raise NaoEncontradoExcecao("Não há  produto com este id")
    else: 
        return(id_produto)








#DELETAR
async def delete_produto(id: str):
   
    produto_deletado = await produtos_persistencia.delete_produto(id)
    
    if produto_deletado.deleted_count:
        return{'status': 'Produto deletado com sucesso!'}
    else: 
        return{ 'status': 'Produto inexistente'}    
