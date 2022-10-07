

from typing import List, Optional
from uuid import uuid4

from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
from games.modelos.cliente import (Cliente)
from games.regras.excecoes import (NaoEncontradoExcecao,
                                            OutroRegistroExcecao)


async def pesquisar_por_email(
    email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False
) -> Optional[dict]:
   clientes = await clientes_persistencia.pesquisar_pelo_email(email)
   if not clientes and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Cliente não encontrada")
   return clientes


async def pesquisar_por_todos() -> List[dict]:
    todos = await clientes_persistencia.pesquisar_todos()
    return todos


async def validar_novo_cliente(clientes: Cliente):  
    outro_cliente = await clientes_persistencia.pesquisar_pelo_email(clientes.email)
    if outro_cliente is not None:
        raise OutroRegistroExcecao("Há outro cliente cadastrado com este email")


async def inserir_novo_cliente(clientes: Cliente) -> Cliente: 
    await validar_novo_cliente(clientes)  
    novo_cliente = clientes.dict()
    
    novo_cliente[clientes_persistencia.Cliente.email] = str(uuid4())

    await clientes_persistencia.inserir_um_novo_cliente(novo_cliente)

    cliente_geral = Cliente(**novo_cliente)

    return cliente_geral