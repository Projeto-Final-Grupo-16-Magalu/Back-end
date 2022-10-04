"""
Regras e ajustes para clientes.
"""

from typing import List, Optional
from uuid import uuid4

import games.persistencia.clientes_persistencia as clientes_persistencia
from games.modelos.cliente import (Cliente)
from games.regras.regras_excecoes import (NaoEncontradoExcecao,
                                            OutroRegistroExcecao)


async def pesquisar_por_email(
    email: str, lanca_excecao_se_nao_encotrado: bool = False
) -> Optional[dict]:
   clientes = await clientes_persistencia.pesquisar_pelo_email(email)
   if not clientes and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Cliente não encontrada")
   return clientes


async def pesquisar_por_todos() -> List[dict]:
    todos = await clientes_persistencia.pesquisar_todos()
    return todos


async def validar_novo_cliente(clientes: Cliente):  
    
    # Seria bom validarmos aqui se há nome e email.
    # Mas como a camada _rest já fez isto para nós, vamos 'confiar'
    # nela.
    # Validando se não há outro  cliente com este email
    outro_cliente = await clientes_persistencia.pesquisar_pelo_email(clientes.email)
    if outro_cliente is not None:
        raise OutroRegistroExcecao("Há outro cliente cadastrado com este email")


async def inserir_novo_cliente(clientes: Cliente) -> Cliente # ***que original era ->ModeloGeralClientes
    await validar_novo_cliente(clientes)  
    # 'Convertendo' cliente para ser salva no banco
    novo_cliente = clientes.dict()
    
    # Gerando novo código com uuidv4  *** (coloquei email para substituir o "código" que não é necessário)
    novo_cliente[clientes_persistencia.Cliente.EMAIL] = str(uuid4())

    # Salvando no banco de dados
    await clientes_persistencia.inserir_um_novo_cliente(novo_cliente)

    # Retornando o registro do cliente completo ***  
    cliente_geral = Cliente(**novo_cliente) #***original seria cliente_geral=ModeloClienteGeral

    return cliente_geral