from typing import Optional
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco, EnderecosCliente
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_ENDERECOS, COLECAO_ENDERECOS_CLIENTE
from games.logs import logger

async def pesquisar_enderecos_por_email(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
           'cliente': email
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        enderecos = await colecao.find_one(filtro, {'_id': 0})
        return enderecos
    except Exception as error:
        logger.exception(error)

async def pesquisar_enderecos_do_cliente(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
            'cliente': email,
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        enderecos = await colecao.find_one(filtro, {'_id': 0})
        return enderecos
    except Exception as error:
        logger.exception(error)

async def adiciona_endereco_lista(email: EmailStr, endereco: Endereco):
    try:
        filtro = {
            'cliente': email
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        atualizacao = {
            '$push': {
                'enderecos': endereco
            }}
        operacao_atualizacao = await colecao.update_one(filtro, atualizacao)
        if operacao_atualizacao.modified_count > 0:
            enderecos_cliente = await pesquisar_enderecos_do_cliente(email)
            logger.info(f'enderecos_atualizados={enderecos_cliente}')
            return enderecos_cliente
        return None
    except Exception as error:
        logger.exception(error)

async def validar_lista_enderecos(email_cliente, endereco: Endereco):
    try:
        filtro = {
            'cliente': email_cliente,
            'enderecos': { '$elemMatch':
                            {'cep': endereco['cep'],
                             'numero': endereco['numero']
                            }
            }
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        endereco_existente = await colecao.find_one(filtro)
        return endereco_existente
    except Exception as e:
        logger.exception(e)

async def pesquisar_enderecos(endereco: Endereco) -> Optional[dict]:
    try:
        filtro = {
           'cep': endereco.cep,
           'numero': endereco.numero
        }
        colecao = obter_colecao(COLECAO_ENDERECOS)
        endereco_pesquisado = await colecao.find_one(filtro)
        return endereco_pesquisado
    except Exception as error:
        logger.exception(error)

async def inserir_novo_endereco(novo_endereco: dict) -> dict:
    try:
        colecao = obter_colecao(COLECAO_ENDERECOS)
        await colecao.insert_one(novo_endereco)
        return novo_endereco
    except Exception as error:
        logger.exception(error)

async def cadastrar_novo_endereco(email: EmailStr, novo_endereco: dict) -> dict:
    try:
        endereco = EnderecosCliente(cliente=email, enderecos=[Endereco(**novo_endereco)])
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        operacao_insercao = await colecao.insert_one(endereco)
        logger.info(f'status={operacao_insercao.acknowledged}')
        return novo_endereco
    except Exception as error:
        logger.exception(error)


async def remover_endereco_do_cliente_por_id(email: EmailStr, id_endereco: str) -> dict:
    try:
        filtro = {
        {'email': email},
        {'$set': id_endereco}
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        enderecos = await colecao.deleteOne(filtro)
        return enderecos
    except Exception as error:
        logger.exception(error)


async def cadastrar_documento_cliente(email: EmailStr):
    documento = {
        'cliente': email,
        'enderecos': []
    }
    colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
    operacao_insercao = await colecao.insert_one(documento)
    logger.info(f'status={operacao_insercao.acknowledged}')
    return operacao_insercao.acknowledged

async def pesquisar_endereco_entrega():
    ...




# colecao = obter_colecao(COLECAO_ENDERECOS)


# async def pesquisar_endereço_por_email(email: EmailStr) -> Optional[dict]:
#     filtro = {
#         'cliente': email
#     }
#     enderecos = await colecao.find_one(filtro)
#     return enderecos


# async def inserir_um_novo_endereco(email: EmailStr, novo_endereco: dict) -> dict:
#     filtro = {
#         'cliente': email
#     }
#     atualizacao = {'$push': {'enderecos': novo_endereco}}
#     await colecao.insert_one(filtro, atualizacao)
#     enderecos = await colecao.find_one(filtro)
#     return enderecos

# async def define_endereco_entrega(email: EmailStr):
#     endereco = await pesquisar_endereço_por_email(email)
#     return endereco


