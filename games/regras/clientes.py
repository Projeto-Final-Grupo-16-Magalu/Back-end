from fastapi import HTTPException
from pydantic import EmailStr
from typing import List, Optional

import games.persistencia.clientes as clientes_persistencia
from games.modelos.cliente import Cliente
from games.logs import logger


async def pesquisar_por_email(email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
   cliente = await clientes_persistencia.pesquisar_pelo_email(email)
   if cliente == None and lanca_excecao_se_nao_encotrado:
        logger.warning(f'Cliente não encontrado : email={email}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Cliente não encontrado')       
   return cliente

async def pesquisar_clientes() -> List[dict]:
    clientes = await clientes_persistencia.pesquisar_clientes()
    logger.info(clientes)
    return clientes

async def validar_novo_cliente(novo_cliente: Cliente):  
    outro_cliente = await clientes_persistencia.pesquisar_pelo_email(novo_cliente.email)
    if outro_cliente is not None:
        logger.warning(f'E-mail cadastrado para outro cliente: {outro_cliente}')
        # Conflict
        raise HTTPException(status_code=409, detail=f'Já existe um cliente cadastrado com esse email')    

async def inserir_novo_cliente(cliente: Cliente): 
    await validar_novo_cliente(cliente)  
    novo_cliente = cliente.dict()
    novo_cliente = await clientes_persistencia.inserir_um_novo_cliente(novo_cliente)
    logger.info(novo_cliente)
    return Cliente(**novo_cliente)