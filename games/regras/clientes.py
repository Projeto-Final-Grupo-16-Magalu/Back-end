from typing import List, Optional
from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
from games.modelos.cliente import Cliente
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.logs import logger


async def pesquisar_por_email(email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
   clientes = await clientes_persistencia.pesquisar_pelo_email(email)
   if not clientes and lanca_excecao_se_nao_encotrado:
        logger.warning(f'Cliente não encontrada: {email}')
        raise NaoEncontradoExcecao("Cliente não encontrada")
   return clientes


async def pesquisar_por_todos() -> List[dict]:
    clientes = await clientes_persistencia.pesquisar_todos()
    logger.info(clientes)
    return clientes


async def validar_novo_cliente(novo_cliente: Cliente):  
    outro_cliente = await clientes_persistencia.pesquisar_pelo_email(novo_cliente.email)
    if outro_cliente is not None:
        logger.warning(f'E-mail cadastrado para outro cliente: {outro_cliente}')
        raise OutroRegistroExcecao("Há outro cliente cadastrado com este email")



async def inserir_novo_cliente(cliente: Cliente): 
    await validar_novo_cliente(cliente)  
    novo_cliente = cliente.dict()
    novo_cliente = await clientes_persistencia.inserir_um_novo_cliente(novo_cliente)
    logger.info(novo_cliente)
    return Cliente(**novo_cliente)