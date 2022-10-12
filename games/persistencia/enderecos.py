

from types import CellType
from typing import List, Optional
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco, EnderecosCliente
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_ENDERECOS, COLECAO_ENDERECOS_CLIENTE


async def pesquisar_endereco_por_email(email: EmailStr) -> Optional[dict]:
    try:
        filtro = {
            EnderecosCliente.email: email
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        enderecos = await colecao.find_one(filtro)
        return enderecos
    except Exception as error:
        print(f'pesquisa_endereco_por_email.erro: {error}')
        

async def pesquisar_enderecos(endereco) -> Optional[dict]:
    try:
        filtro = {
            Endereco.cep: cep,
            Endereco.numero: numero
        }
        colecao = obter_colecao(COLECAO_ENDERECOS)
        enderecos = await colecao.find_one(filtro)
        return enderecos
    except Exception as error:
        print(f'pesquisa_endereco_por_email.erro: {error}')
        
async def inserir_novo_endereco(novo_endereco: dict) -> dict:
    try:
        colecao = obter_colecao(COLECAO_ENDERECOS)
        await colecao.insert_one(novo_endereco)
        return novo_endereco
    except Exception as error:
        print(f'inserir_novo_endereco.erro: {e}')


async def remover_endereco_do_cliente_por_id(email: Emailstr, id_endereco: _id) -> dict:
    try:
        filtro = {
        {'email': email},
        {'$set': id_endereco}
        }
        colecao = obter_colecao(COLECAO_ENDERECOS_CLIENTE)
        enderecos = await colecao.deleteOne(filtro)
        return enderecos
    except Exception as error:
        print(f'remover_endereco.erro: {e}')