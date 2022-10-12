
from typing import List, Optional
from uuid import uuid4
from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
import games.persistencia.enderecos as enderecos_persistencia
from games.modelos.endereco import Endereco, EnderecosCliente
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.regras.clientes import pesquisar_por_email

async def pesquisar_enderecos_por_email(email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
    endereco = await enderecos_persistencia.pesquisar_endereço_por_email(email/)
    if not endereco and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Cliente não encontrado")
    return endereco

async def validar_novo_endereco(endereco:Endereco, email: EmailStr):
    outro_endereco = await enderecos_persistencia.pesquisar_endereços(endereco)
    if outro_endereco is not None:
            raise OutroRegistroExcecao('Esse endereço já foi cadastrado')
    return outro_endereco
        
    
async def inserir_novo_endereco(endereco: Endereco) -> Endereco:
        await validar_novo_endereco(endereco)
        outro_endereco = endereco.dict()
        await enderecos_persistencia.inserir_novo_endereco(outro_endereco)
        return endereco

async def cadastrar_novo_endereco_para_cliente(email: EmailStr, endereco: Endereco)
    cliente = await clientes_persistencia.pesquisar_por_email(email)
        if cliente == None:
            raise NaoEncontradoExcecao('Cliente não cadastrado.')
        novo_endereco = await enderecos_persistencia.pesquisar_enderecos_do_cliente(email)
            if not novo_endereco:
            return await enderecos_persistencia.cadastrar_novo_endereco(endereco)
        if endereco in novo_endereco:
            raise OutroRegistroExcecao('Esse endereço já foi cadastrado para esse cliente')

async def remover_endereco_do_cliente_por_id(email: Emailstr, id_endereco: _id):
    endereco_deletar = await enderecos_persistencia.pesquisar_endereco_por_email(email, id_endereco)
    if id_endereco in endereco_deletar:
        return await enderecos_persistencia.remover_endereco_do_cliente_por_id(email, id_endereco)
    raise NaoEncontradoExcecao('Endereço não cadastrado para esse cliente.')