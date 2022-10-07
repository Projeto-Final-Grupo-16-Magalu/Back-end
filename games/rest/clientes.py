from typing import List

import games.regras.clientes as clientes_regras
from fastapi import APIRouter, status
from games.modelos.cliente import (Cliente) 
                             

# Minha rota API de clientes
rota_clientes = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/clientes"
)


# Cria nova cliente
@rota_clientes.post(
    "/",

    status_code=status.HTTP_201_CREATED,
     response_model= Cliente, 
)
async def criar_novo_cliente(clientes:Cliente):
    novo_cliente = await clientes_regras.inserir_novo_cliente(clientes)
    return novo_cliente


# Pesquisa cliente pelo email.
@rota_clientes.get(
    "/{email}",
    
    response_model = Cliente
)
async def pesquisar_cliente_pelo_email(email: str):
    cliente = await clientes_regras.pesquisar_por_email(email, True)
    return cliente


# Pesquisa por todos os clientes (sem um filtro)
@rota_clientes.get(
    "/",
    
     response_model=List[Cliente] 
)
async def pesquisar_todos_os_clientes() -> List[Cliente]:  
    todos = await clientes_regras.pesquisar_por_todos()
    return todos