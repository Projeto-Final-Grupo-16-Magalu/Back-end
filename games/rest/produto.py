from typing import List
from fastapi import APIRouter
from games.modelos.produto import AtualizacaoProduto, Produto

import games.regras.produto as produto_regras
import games.persistencia.produtos as produto_persistencia

rota_produto = APIRouter(
    prefix='/api/produtos',
    tags = ['Produtos']
)


# 1.Cadastrar um produto
@rota_produto.post('/')
async def criar_novo_produto(produto: Produto):
    novo_produto= await produto_regras.inserir_novo_produto(produto)
    return novo_produto


# 2.Atualizar os dados de um produto
@rota_produto.put('/{codigo}')
async def atualizar_produto(codigo: str, produto: AtualizacaoProduto):
    produto = await produto_regras.atualizar_por_codigo(codigo, produto)
    return produto


# 3.Pesquisar um produto pelo id
@rota_produto.get('/{id}')
async def pesquisar_pelo_id(id: str):
    produto = await produto_regras.pesquisar_pelo_id(id)
    return produto


# 3.Pesquisar um produto pelo codigo
@rota_produto.get('/codigo/{codigo}')
async def pesquisar_pelo_codigo(codigo: int):
    produto = await produto_regras.pesquisar_pelo_codigo(codigo)
    return produto


# 4.Pesquisar um produto pelo nome
@rota_produto.get('/nome/{nome}')
async def pesquisar_pelo_nome(nome_produto: str):
    produto = await produto_regras.pesquisar_pelo_nome(nome_produto)
    return  produto


# 5.Remover um produto (Opcional)
@rota_produto.delete('/{id}')
async def delete_produto(id: str):
    removeu =  await produto_regras.delete_produto(id)
    return removeu

@rota_produto.get('/todos/produtos')
#teste produto
async def pesquisar_todos_os_produto() -> List[Produto]:
    produtos = await produto_persistencia.pesquisar_produtos()
    return produtos