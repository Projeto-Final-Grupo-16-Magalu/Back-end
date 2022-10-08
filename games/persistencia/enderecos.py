

from typing import List, Optional

from pydantic import EmailStr
from games.modelos.cliente import Cliente
from games.servidor.database import (DataBase, connect_db)
from games.modelos.endereco import Endereco, EnderecosCliente


COLECAO_ENDERECOS = connect_db()

db = DataBase()

async def pesquisar_endereço_por_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        Cliente.email: email
    }
    enderecos = await COLECAO_ENDERECOS.find(filtro)
    return enderecos


async def inserir_um_novo_endereco(novo_endereco: dict) -> dict:
    await COLECAO_ENDERECOS.insert_one(novo_endereco)
    return novo_endereco