from typing import List

import games.regras.clientes_regras as clientes_regras
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
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED,
    # Modelo da resposta *** original: response_model = ModeloCodigoMusica ***(codigo = mudei para "email")
     response_model= Cliente, 
)
async def criar_novo_cliente(clientes: Cliente):
    novo_cliente = await clientes_regras.inserir_novo_cliente(clientes)
    return novo_cliente

# Atualiza a música pelo código. #*** atualiza cliente pelo email**** vamos usar id?
@rota_clientes.put("/{email}")
async def atualizar_cliente(email: str, cliente: dict):
    return None


# Remove cliente pelo email
@rota_clientes.delete("/{email}")
async def remover_cliente(email: str):
    return None


# Pesquisa o cliente pelo email.
@rota_clientes.get(
    "/{email}",
    # Informamos para a pesquisa o modelo da resposta
    response_model = Cliente #**original seria response_model=GeralMusica(com informaçoes da classe ModeloMusicaBase e ModeloCodigoMusica)
)
async def pesquisar_cliente_pelo_email(email: str):
    cliente = await clientes_regras.pesquisar_por_email(email, True)
    return cliente


# Pesquisa por todos os clientes (sem um filtro)
@rota_clientes.get(
    "/",
    # E também informamos aqui o modelo da resposta.
     response_model=List[Cliente] #**original seria [GeralMusica](com informaçoes da classe ModeloMusicaBase e ModeloCodigoMusica)
)
async def pesquisar_todos_os_clientes() -> List[Cliente]:  #**original seria [GeralMusica](com informaçoes da classe ModeloMusicaBase e ModeloCodigoMusica)
    todos = await clientes_regras.pesquisar_por_todos()
    return todos