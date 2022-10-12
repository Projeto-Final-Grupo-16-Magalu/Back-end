from fastapi import HTTPException
from typing import Optional
from pydantic.networks import EmailStr

from games.logs import logger
from games.modelos.endereco import Endereco
from games.regras.excecoes import NaoEncontradoExcecao

import games.persistencia.clientes as clientes_persistencia
import games.persistencia.enderecos as enderecos_persistencia


async def pesquisar_enderecos_por_email(email: EmailStr) -> Optional[dict]:
    endereco = await enderecos_persistencia.pesquisar_enderecos_por_email(email)
    if not endereco:
        logger.warning(f'Cliente não encontrado : email={email}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Cliente não encontrado')
    return endereco


async def validar_novo_endereco(endereco: Endereco):
    outro_endereco = await enderecos_persistencia.pesquisar_enderecos(endereco)
    if outro_endereco is not None:
       return True
    return False


async def inserir_novo_endereco(endereco: Endereco, email: EmailStr):
        # Verifica se o endereço já está cadastrado na coleção de endereços
        # Um mesmo endereço pode estar vinculado a mais de um usuário
        endereco_existe = await validar_novo_endereco(endereco)
        if not endereco_existe:
            await enderecos_persistencia.inserir_novo_endereco(endereco.dict())
        enderecos = await cadastrar_novo_endereco_para_cliente(email, endereco.dict())
        return enderecos


async def cadastrar_novo_endereco_para_cliente(email: EmailStr, endereco: Endereco):
    logger.info(f'email={email} : endereco={endereco}')
    # Verificar se o cliente existe
    cliente = await clientes_persistencia.pesquisar_pelo_email(email)
    if cliente == None:
        logger.warning(f'Cliente não cadastrado : email={email}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Cliente não cadastrado')
    # Verificar se o endereço já está cadastrado na lista de endereços do cliente
    endereco_existente = await enderecos_persistencia.validar_lista_enderecos(email, endereco)
    # Adiciona endereço caso não exista na lista de endereços do cliente
    # Caso contrário, retorna um erro
    if endereco_existente != None:
        logger.warning(f'Endereço já cadastrado para o cliente : email={email}')
        # Conflict
        raise HTTPException(status_code=409, detail=f'Endereço já cadastrado para o cliente')
    enderecos_cliente = await enderecos_persistencia.adiciona_endereco_lista(email, endereco)
    logger.info(f'enderecos={enderecos_cliente}')
    return enderecos_cliente


async def remover_endereco_do_cliente_por_id(email: EmailStr, id_endereco: str):
    endereco_deletar = await enderecos_persistencia.pesquisar_endereco_por_email(email, id_endereco)
    if id_endereco in endereco_deletar:
        return await enderecos_persistencia.remover_endereco_do_cliente_por_id(email, id_endereco)
    raise NaoEncontradoExcecao('Endereço não cadastrado para esse cliente.')