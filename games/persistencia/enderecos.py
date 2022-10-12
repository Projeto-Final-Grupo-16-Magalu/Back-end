from typing import Optional
from pydantic.networks import EmailStr

from games.configuracoes import COLECAO_ENDERECOS, COLECAO_ENDERECOS_CLIENTE
from games.logs import logger
from games.modelos.endereco import Endereco, EnderecosCliente
from games.servidor.database import obter_colecao


colecao_enderecos = obter_colecao(COLECAO_ENDERECOS)
colecao_enderecos_clientes = obter_colecao(COLECAO_ENDERECOS_CLIENTE)


async def pesquisar_enderecos_por_email(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
           'cliente': email
        }
        enderecos = await colecao_enderecos_clientes.find_one(filtro, {'_id': 0})
        return enderecos
    except Exception as error:
        logger.exception(error)

async def pesquisar_enderecos_do_cliente(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
            'cliente': email,
        }
        enderecos = await colecao_enderecos_clientes.find_one(filtro, {'_id': 0})
        return enderecos
    except Exception as error:
        logger.exception(error)


async def adiciona_endereco_lista(email: EmailStr, endereco: Endereco):
    try:
        filtro = {
            'cliente': email
        }
        atualizacao = {
            '$push': {
                'enderecos': endereco
            }}
        operacao_atualizacao = await colecao_enderecos_clientes.update_one(filtro, atualizacao)
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
        endereco_existente = await colecao_enderecos_clientes.find_one(filtro)
        return endereco_existente
    except Exception as e:
        logger.exception(e)


async def pesquisar_enderecos(endereco: Endereco) -> Optional[dict]:
    try:
        filtro = {
           'cep': endereco.cep,
           'numero': endereco.numero
        }
        endereco_pesquisado = await colecao_enderecos.find_one(filtro)
        return endereco_pesquisado
    except Exception as error:
        logger.exception(error)


async def inserir_novo_endereco(novo_endereco: dict) -> dict:
    try:
        await colecao_enderecos.insert_one(novo_endereco)
        return novo_endereco
    except Exception as error:
        logger.exception(error)


async def cadastrar_novo_endereco(email: EmailStr, novo_endereco: dict) -> dict:
    try:
        endereco = EnderecosCliente(cliente=email, enderecos=[Endereco(**novo_endereco)])
        operacao_insercao = await colecao_enderecos_clientes.insert_one(endereco)
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
        enderecos = await colecao_enderecos_clientes.delete_one(filtro)
        return enderecos
    except Exception as error:
        logger.exception(error)


async def cadastrar_documento_cliente(email: EmailStr):
    documento = {
        'cliente': email,
        'enderecos': []
    }
    operacao_insercao = await colecao_enderecos_clientes.insert_one(documento)
    logger.info(f'status={operacao_insercao.acknowledged}')
    return operacao_insercao.acknowledged


async def pesquisar_endereco_entrega(email: EmailStr):
    enderecos = await pesquisar_enderecos_por_email(email)
    logger.info(f'enderecos={enderecos}')
    # Verifica se existem endereços cadastrados para o cliente
    # Verifica se existe a chave 'enderecos' no dicionário retornado
    # Percorre a lista de endereços
    # Retorna o primeiro objeto da lista que possui entrega como true
    if enderecos != None and 'enderecos' in enderecos:
        for endereco in enderecos['enderecos']:
            if endereco['entrega'] == True:
                logger.info(f'endereco_entrega={endereco}')
                return endereco
    return None

