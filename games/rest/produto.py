from typing import List
from unittest import result
from fastapi import APIRouter
from games.configuracoes import COLECAO_PRODUTOS
from games.modelos import produto
from games.modelos.produto import AtualizacaoProduto, Produto
import games.regras.produto as produto_regras
import games.persistencia.produtos as produto_persistencia

rota_produto = APIRouter(
    prefix="/api/produto"
)

# 1.Cadastrar um produto
@rota_produto.post("/")
async def criar_novo_produto(produto: Produto):
    novo_produto= await produto_regras.inserir_novo_produto(produto)
    return novo_produto

# 2.Atualizar os dados de um produto.
@rota_produto.put("/{codigo}")
async def atualizar_produto(codigo: str, produto: AtualizacaoProduto):
    produto = await produto_regras.atualizar_por_codigo(codigo, produto)
    return produto

# 3.Pesquisar um produto.
@rota_produto.get("/{id}")
async def pesquisar_pelo_codigo(id_produto: str):
    produto = await produto_regras.validar_id_produto(id_produto)
    return  Produto(**produto)

# 4.Pesquisar um produto pelo nome.
@rota_produto.get("/nome/{nome_produto}")
async def pesquisar_pelo_nome(nome_produto: str):
    produto = await produto_persistencia.pesquisar_pelo_nome(nome_produto)
    return  Produto(**produto)

# 5.Remover um produto. (Opcional)
@rota_produto.delete("/{id_produto}")
async def delete_produto(id_produto: str):
    removeu =  await produto_regras.delete_produto(id_produto)
    return removeu


   
