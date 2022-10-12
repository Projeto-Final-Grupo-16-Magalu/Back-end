from typing import List, Optional
from pydantic.networks import EmailStr

from games.modelos.cliente import Cliente
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_CLIENTES
   
   
async def pesquisar_pelo_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        "email": email
    }
    cliente = await obter_colecao(COLECAO_CLIENTES).find_one(filtro, {'_id': 0} )
    return cliente

async def pesquisar_todos() -> List[dict]:
    filtro = {}
    cursor_pesquisa = obter_colecao(COLECAO_CLIENTES).find(filtro)
    lista_todos = [
        clientes
        async for clientes in cursor_pesquisa
    ]
    return lista_todos

async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    filtro = {
        Cliente.nome : nome
    }
    colecao = obter_colecao(COLECAO_CLIENTES)
    clientes = await colecao.find_one(filtro)
    return clientes


async def inserir_um_novo_cliente(novo_cliente: dict) -> dict: 
    colecao = obter_colecao(COLECAO_CLIENTES)
    await colecao.insert_one(novo_cliente)
    return novo_cliente