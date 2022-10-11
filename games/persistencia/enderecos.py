from games.configuracoes import COLECAO_ENDERECOS
from games.servidor.database import obter_colecao

from typing import Optional
from pydantic import EmailStr
from games.modelos.cliente import Cliente


colecao = obter_colecao(COLECAO_ENDERECOS)


async def pesquisar_endereço_por_email(email: EmailStr) -> Optional[dict]:
    filtro = {
        'cliente': email
    }
    enderecos = await colecao.find_one(filtro)
    return enderecos


async def inserir_um_novo_endereco(email: EmailStr, novo_endereco: dict) -> dict:
    filtro = {
        'cliente': email
    }
    enderecos = await colecao.find_one(filtro)
    atualizacao = {'$push': {'enderecos': novo_endereco}}
    await colecao.insert_one(filtro, atualizacao)
    return enderecos
