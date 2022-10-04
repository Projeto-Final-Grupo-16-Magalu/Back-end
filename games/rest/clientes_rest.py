from typing import List

import clientes.regras.clientes_regras as clientes_regras
from fastapi import APIRouter, status
from clientes.modelos import (ModeloBaseClientes,ModeloEmailClientes,
                             ModeloGeralClientes)

# Minha rota API de músicas
rota_clientes = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/musicas"
)


# Cria nova cliente
@rota_clientes.post(
    "/",
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED,
    # Modelo da resposta
    response_model=ModeloEmailClientes,
)
async def criar_novo_cliente(clientes: ModeloBaseClientes):
    novo_cliente = await clientes_regras.inserir_novo_cliente(clientes)
    return novo_cliente

# Atualiza a música pelo código. #*** atualiza cliente pelo email****
@rota_clientes.put("/{email}")
async def atualizar_cliente(email: str, cliente: dict):
    return None


# Remove uma música pelo código *remove cliente pelo email
@rota_clientes.delete("/{email}")
async def remover_cliente(email: str):
    return None


# Pesquisa o cliente pelo email.
@rota_clientes.get(
    "/{email}",
    # Informamos para a pesquisa o modelo da resposta
    response_model=ModeloGeralClientes
)
async def pesquisar_cliente_pelo_email(email: str):
    cliente = await clientes_regras.pesquisar_por_email(email, True)
    return cliente


# Pesquisa por todos os clientes (sem um filtro)
@rota_clientes.get(
    "/",
    # E também informamos aqui o modelo da resposta.
    response_model=List[ModeloGeralClientes]
)
async def pesquisar_todos_os_clientes() -> List[ModeloGeralClientes]:
    todos = await clientes_regras.pesquisar_por_todos()
    return todos