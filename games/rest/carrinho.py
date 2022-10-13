from fastapi import APIRouter, status
from pydantic import EmailStr

import games.regras.carrinho as carrinho_regras
from games.modelos.carrinho import AbrirCarrinho, Carrinho, ItemCarrinho, ErroCarrinhoNaoCriado, ErroCarrinhoJaCriado ErroCarrinhoNaoFechado, ErroProdutoNaoDisponivel, ErroProdutoNaoEncontrado, ErroCarrinhoJaRemovido, ErroCarrinhoNaoRemovido
from games.rest.documentacao import DESCRICAO_CRIAR_CARRINHO_ABERTO, ADICIONAR_ITEM_CARRINHO_ABERTO

# Minha rota API de carrinhos
rota_carrinho = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/carrinho-compras",
    tags = ["Carrinho"]
)


# Cria um carrinho de compras aberto
@rota_carrinho.post(
    "/",
    summary= "Criar um carrinho de compras aberto",
    description= DESCRICAO_CRIAR_CARRINHO_ABERTO,
    status_code=status.HTTP_201_CREATED,
    response_model=Carrinho,
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Já existe um cliente cadastrado com esse email",
            "model": ErroCarrinhoJaCriado
        },
        status.HTTP_404_NOT_FOUND:{
            "description": "Já existe um cliente cadastrado com esse email",
            "model": ErroCarrinhoJaCriado
        }
    }
)
async def criar_novo_carrinho(carrinho: AbrirCarrinho):
    carrinho_criado = await carrinho_regras.criar_novo_carrinho(carrinho)
    return carrinho_criado

# Atualiza quantidade de itens do carrinho
@rota_carrinho.put(
    "/adicionar_item"
    summary= "Adicionar item a um carrinho de compras aberto",
    description= ADICIONAR_ITEM_CARRINHO_ABERTO,
    status_code=status.HTTP_200_OK,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Produto não encontrado",
            "model": ErroProdutoNaoEncontrado},
        status.HTTP_410_GONE:{
            "description": "Produto não está mais disponível",
            "model": ErroProdutoNaoDisponivel  
        }
)
async def adicionar_item_carrinho(email_cliente: str, item_carrinho: ItemCarrinho):
    carrinho_atualizado = await carrinho_regras.adicionar_item_carrinho(email_cliente, item_carrinho)
    return carrinho_atualizado


# Fecha um carrinho aberto
@rota_carrinho.put(
    "/fechar/{email_cliente}",
    summary= "Fechar um carrinho aberto ",
    description= DESCRICAO_FECHAR_CARRINHO_ABERTO,
    status_code=status.HTTP_200_OK,
    response_model = Carrinho,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Não foi possível fechar o carrinho",
            "model": ErroCarrinhoNaoFechado}    
        }
)
async def fechar_carrinho(email_cliente: EmailStr):
    status_carrinho = await carrinho_regras.fechar_carrinho(email_cliente)
    return status_carrinho

# Remove um carrinho (Opcional)
@rota_carrinho.delete(
    "/{email_cliente}",
    summary= "Remover um carrinho aberto",
    description= DESCRICAO_REMOVER_CARRINHO_ABERTO,
    status_code=status.HTTP_200_OK,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Não foi possível remover o carrinho",
            "model": ErroCarrinhoNaoRemovido},
        status.HTTP_410_GONE:{
            "description": "O carrinho já foi removido",
            "model": ErroCarrinhoJaRemovido}    
        })
async def remover_carrinho(email_cliente: EmailStr):
    return(f'remover_carrinho {email_cliente}')

# Consulta carrinho de compras aberto de um cliente
@rota_carrinho.get(
    "/{email_cliente}",
    summary= "Consultar um carrinho aberto",
    description= DESCRICAO_PESQUISAR_CARRINHO_ABERTO,
    status_code=status.HTTP_200_OK,
    response_model = Carrinho,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Não foi encontrado carrinho para esse cliente",
            "model": ErroCarrinhoNaoCriado}  
       }
)
async def pesquisar_carrinho(email_cliente: EmailStr):
    return(f'pesquisar_carrinho: cliente: {email_cliente}')

# Consulta os carrinhos de compra fechados de um cliente (Opcional)
# Consulta os produtos e suas quantidades em carrinhos fechados (Opcional)
# Consulta quantos carrinhos fechados os clientes possuem (Opcional)
@rota_carrinho.get(
    "/fechados/{email_cliente}",
    summary= "Consultar carrinhos fechado",
    description= DESCRICAO_PESQUISAR_CARRINHOS_FECAHADOS,
    status_code=status.HTTP_200_OK,
    response_model = Carrinho,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Não foram encontrados carrinhos fecahdos para esse cliente",
            "model": ErroCarrinhosFecahdosNaoExistem}  
       }
) 
async def pesquisar_carrinhos_fechados(email_cliente: EmailStr):
    return(f'pesquisar_carrinhos_fechados: cliente: {email_cliente}')