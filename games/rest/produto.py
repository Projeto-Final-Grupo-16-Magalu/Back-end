from typing import List
from unittest import result
from fastapi import APIRouter
from games.configuracoes import COLECAO_PRODUTOS
from games.modelos import produto
from games.modelos.carrinho import ErroProdutoNaoEncontrado
from games.modelos.produto import AtualizacaoProduto, Produto, ErroNomeJaCadastrado, ErroNomeJaRemovido, ErroProdutoJaCadastrado
import games.regras.produto as produto_regras
import games.persistencia.produtos as produto_persistencia
from games.rest.documentacao import DESCRICAO_CADASTRAR_PRODUTO, DESCRICAO_ATUALIZAR_DADOS_PRODUTO, DESCRICAO_PESQUISAR_PRODUTO_ID, DESCRICAO_PESQUISAR_PRODUTO_NOME, DESCRICAO_REMOVER_PRODUTO
# Minha rota API de produtos
rota_produtos = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/produto",
    tags = ["Produto"]
)

# Cadastrar um produto
@rota_produto.post(
    "/",
    summary= "Cadastro um novo produto",
    description= DESCRICAO_CADASTRAR_PRODUTO,
    status_code=status.HTTP_201_CREATED,
    response_model= Produto, 
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Esse produto já foi cadastrado",
            "model": ErroProdutoJaCadastrado
        }
    }
)
async def criar_novo_produto(produto: Produto):
    novo_produto = await produto_regras.inserir_novo_produto(produto)
    return novo_produto

# Atualizar os dados de um produto.
@rota_produto.put(
    "/{codigo}",
    summary= "Atualizar os dados de um produto",
    description= DESCRICAO_ATUALIZAR_DADOS_PRODUTO,
    status_code=status.HTTP_200_OK,
    response_model= Produto, 
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Já existe um produto com esse nome",
            "model": ErroNomeJaCadastrado
        }
    }
)
async def atualizar_produto(codigo: str, produto: AtualizacaoProduto):
    produto = await produto_regras.atualizar_por_codigo(codigo, produto)
    return produto

# Pesquisar um produto.
@rota_produto.get(
    "/{id}",
    summary= "Pesquisar um produto pelo id",
    description= DESCRICAO_PESQUISAR_PRODUTO_ID,
    status_code=status.HTTP_200_OK,
    response_model= Produto, 
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Produto não encontrado",
            "model": ErroProdutoNaoEncontrado
        }
    }
)
async def pesquisar_pelo_codigo(id_produto: str):
    produto = await produto_regras.validar_id_produto(id_produto)
    return  Produto(**produto)

# 4.Pesquisar um produto pelo nome.
@rota_produto.get(
    "/nome/{nome_produto}",
    summary= "Pesquisar um produto pelo nome",
    description= DESCRICAO_PESQUISAR_PRODUTO_NOME,
    status_code=status.HTTP_200_OK,
    response_model= Produto, 
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Produto não encontrado",
            "model": ErroProdutoNaoEncontrado
        }
    }
    )
async def pesquisar_pelo_nome(nome_produto: str):
    produto = await produto_regras.pesquisar_pelo_nome(nome_produto)
    return  Produto(**produto)

# 5.Remover um produto. (Opcional)
@rota_produto.delete(
    "/{id_produto}",
    summary= "Remover um produto pelo id",
    description= DESCRICAO_REMOVER_PRODUTO,
    status_code=status.HTTP_200_OK,
    response_model= Produto, 
    responses = {
        status.HTTP_410_GONE:{
            "description": "Esse produto já foi removido",
            "model": ErroProdutoJaRemovido},
        status.HTTP_404_NOT_FOUND:{
            "description": "Produto não encontrado",
            "model": ErroProdutoNaoEncontrado},
    }
    )
async def delete_produto(id_produto: str):
    removeu =  await produto_regras.delete_produto(id_produto)
    return removeu
