

from typing import List, Optional
from games.modelos.cliente import Cliente
from games.servidor.database import db
from pydantic.networks import EmailStr
   
   
async def pesquisar_pelo_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        "email":email
    }
    clientes = await db.colecao_clientes.find_one(filtro)
    return clientes

async def pesquisar_todos() -> List[dict]:
    filtro = {}
    cursor_pesquisa = db.colecao_clientes.find(filtro)
    lista_todos = [
        clientes
        async for clientes in cursor_pesquisa
    ]
    return lista_todos

async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        Cliente.nome : nome
    }
    clientes = await db.colecao_clientes.find_one(filtro)
    return clientes


async def inserir_um_novo_cliente(novo_cliente: dict) -> dict: 
    await db.colecao_clientes.insert_one(novo_cliente)
    return novo_cliente