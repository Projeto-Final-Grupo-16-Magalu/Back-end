from typing import List
from fastapi import APIRouter
from games.modelos.produto import Produto
import games.regras.produto as produto_regras
import games.persistencia.produtos as produto_persistencia

rota_produto = APIRouter(
    prefix="/api/produto"
)

@rota_produto.post("/")
async def criar_novo_produto(produto: Produto):
    novo_produto= await produto_regras.inserir_novo_produto(produto)
    return novo_produto

@rota_produto.get("/todos")
async def pesquisar_todos_os_produtos() ->List[Produto]:
    todos = await produto_regras.pesquisar_todos_produtos()
    return todos

@rota_produto.get("/{nome_produto}")
async def pesquisar_pelo_nome(nome_produto: str):
    produto = await produto_persistencia.pesquisar_pelo_nome(nome_produto)
    return  Produto(**produto)
