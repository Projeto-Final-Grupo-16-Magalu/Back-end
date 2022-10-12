from fastapi import APIRouter, status
from typing import List

import games.regras.clientes as clientes_regras
from games.modelos.cliente import Cliente, ErroEmailJaCadastrado, ErroClienteNaoEncontrado
from games.rest.documentacao import DESCRICAO_CADASTRAR_CLIENTE, DESCRICAO_PESQUISAR_CLIENTE_POR_EMAIL, DESCRICAO_PESQUISAR_CLIENTES                          

# Minha rota API de clientes
rota_clientes = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/clientes",
    tags = ["Clientes"]
)

# Cria novo cliente
@rota_clientes.post(
    "/",
    summary= "Cadastro de cliente",
    description= DESCRICAO_CADASTRAR_CLIENTE,
    status_code=status.HTTP_201_CREATED,
    response_model= Cliente, 
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Já existe um cliente cadastrado com esse email",
            "model": ErroEmailJaCadastrado
        }
    }
)
async def criar_novo_cliente(cliente: Cliente):
    novo_cliente = await clientes_regras.inserir_novo_cliente(cliente)
    return novo_cliente

# Pesquisa cliente pelo email.
@rota_clientes.get(
    "/{email}",
    summary= "Pesquisa de cliente por email",
    description= DESCRICAO_PESQUISAR_CLIENTE_POR_EMAIL,
    status_code=status.HTTP_200_OK,
    response_model = Cliente,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Cliente não encontrado",
            "model": ErroClienteNaoEncontrado}    
        }
)
async def pesquisar_cliente_pelo_email(email: str):
    cliente = await clientes_regras.pesquisar_por_email(email, True)
    return cliente


# Pesquisa por todos os clientes (sem um filtro)
@rota_clientes.get(
    "/",
    summary= "Pesquisa todos os clientes",
    description= DESCRICAO_PESQUISAR_CLIENTES,
    status_code=status.HTTP_200_OK,
    response_model = List[Cliente],
    responses = {
        status.HTTP_404_NOT_FOUND:{
            "description": "Clientes não encontrados",
            "model": ErroClienteNaoEncontrado}    
        }
)
async def pesquisar_todos_os_clientes() -> List[Cliente]:  
    clientes = await clientes_regras.pesquisar_clientes()
    return clientes