

from typing import List, Optional

from pydantic import EmailStr
from games.modelos.cliente import Cliente
from games.servidor.database import (DataBase, connect_db)
from games.modelos.endereco import Endereco, EnderecosCliente


COLECAO_ENDERECOS = connect_db("enderecos")

db = DataBase()

async def pesquisar_pelo_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        Cliente.email: email
    }
    enderecos = await COLECAO_ENDERECOS.find(filtro)
    return db.colecao_enderecos

async def pesquisar_todos() -> List[dict]:
    filtro = {}
    cursor_pesquisa = COLECAO_ENDERECOS.find(filtro)
    lista_todos = [
       db.colecao_enderecos
        async for enderecos in cursor_pesquisa
    ]
    return lista_todos

async def inserir_um_novo_endereco(novo_endereco: dict) -> dict:
    await COLECAO_ENDERECOS.insert_one(novo_endereco)
    return novo_endereco