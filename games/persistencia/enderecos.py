from types import CellType
from typing import List, Optional
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco, EnderecosCliente
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_ENDERECOS, COLECAO_ENDERECOS_CLIENTE

colecao_enderecoscliente = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
colecao = obter_colecao(COLECAO_ENDERECOS)

async def pesquisar_endereco_por_email(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
            EnderecosCliente.email: email
        }
        enderecos = await colecao_enderecoscliente.find_one(filtro)
        logger.info(enderecos)
        return enderecos
    except Exception as e:
        logger.exception(e)
        
async def pesquisar_enderecos_do_cliente(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
            EnderecosCliente.cep: cep,
            EnderecosCliente.numero: numero
        }
        enderecos = await colecao_enderecoscliente.find_one(filtro)
        logger.info(enderecos)
        return enderecos
    except Exception as e:
        logger.exception(e)
        
async def pesquisar_enderecos(endereco) -> Optional[dict]:
    try:
        filtro = {
            Endereco.cep: cep,
            Endereco.numero: numero
        }
        enderecos = await colecao.find_one(filtro)
        logger.info(enderecos)
        return enderecos
    except Exception as e:
        logger.exception(e)
        
async def inserir_novo_endereco(novo_endereco: dict) -> dict:
    try:
        await colecao.insert_one(novo_endereco)
        logger.info(novo_endereco)
        return novo_endereco
    except Exception as e:
        logger.exception(e)
        
async def cadastrar_novo_endereco(email: EmailStr, novo_endereco: dict) -> dict:
    try:
        try:
        filtro = {
            EnderecosCliente.email: email
        }
        enderecos = await colecao_enderecoscliente.find_one(filtro)
        logger.info(enderecos)
        novo_endereco = await colecao.insert_one(COLECAO_ENDERECOS_CLIENTE)
        logger.info(novo_endereco)
        return novo_endereco
    except Exception as e:
        logger.exception(e)


async def remover_endereco_do_cliente_por_id(email: Emailstr, id_endereco: _id) -> dict:
    try:
        filtro = {
        {'email': email},
        {'$set': id_endereco}
        }
        enderecos = await colecao_enderecoscliente.deleteOne(filtro)
        logger.info(enderecos)
        return enderecos
    except Exception as e:
        logger.exception(e)


async def pesquisar_endereco_entrega():
    ...


