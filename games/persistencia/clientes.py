

from typing import List, Optional
from games.modelos.cliente import Cliente
from games.servidor.database import (connect_db , disconnect_db)
from pydantic.networks import EmailStr
   
COLECAO_CLIENTES = connect_db("clientes")
COLECAO_CLIENTES = disconnect_db("clientes")

async def pesquisar_pelo_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        Cliente.email: email
    }
    clientes = await COLECAO_CLIENTES.find_one(filtro)
    return clientes

async def pesquisar_todos() -> List[dict]:
    filtro = {}
    cursor_pesquisa = COLECAO_CLIENTES.find(filtro)
    lista_todos = [
        clientes
        async for clientes in cursor_pesquisa
    ]
    return lista_todos

async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        Cliente.nome : nome
    }
    clientes = await COLECAO_CLIENTES.find_one(filtro)
    return clientes

async def pesquisar_pelo_id(id_cliente:int ) -> Optional[dict]:
    filtro = {
        Cliente.id_cliente :id_cliente
    }
    clientes = await COLECAO_CLIENTES.find_one(filtro)
    return clientes

async def inserir_um_novo_cliente(novo_cliente: dict) -> dict: 
    await COLECAO_CLIENTES.insert_one(novo_cliente)
    return novo_cliente