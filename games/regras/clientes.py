from typing import List, Optional
from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
from games.modelos.cliente import Cliente
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.logs import logger


# Pesquisa cliente por email 
async def pesquisar_por_email(email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
   #Busca cliente pelo email
   clientes = await clientes_persistencia.pesquisar_pelo_email(email)
   if not clientes and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Cliente não encontrado")
        logger.warning(f'Cliente não encontrada: {email}')
        raise NaoEncontradoExcecao("Cliente não encontrada")
   return clientes

# Pesquisa todos os clientes
async def pesquisar_por_todos() -> List[dict]:
    clientes = await clientes_persistencia.pesquisar_todos()
    logger.info(clientes)
    return clientes

# Verifica se o cliente já existe 
async def validar_novo_cliente(novo_cliente: Cliente):  
    outro_cliente = await clientes_persistencia.pesquisar_pelo_email(novo_cliente.email)
    # Caso o email já esteja cadastrado para um cliente
    if outro_cliente is not None:
        logger.warning(f'E-mail cadastrado para outro cliente: {outro_cliente}')
        raise OutroRegistroExcecao("Há outro cliente cadastrado com este email")
    return outro_cliente

# Cadastra um novo cleinte
async def inserir_novo_cliente(cliente: Cliente): 
    # Verifica se o cliente já existe
    await validar_novo_cliente(cliente)  
    # Caso a validação acima não seja atendida, cadastrar o cliente
    novo_cliente = cliente.dict()
    novo_cliente = await clientes_persistencia.inserir_um_novo_cliente(novo_cliente)
    logger.info(novo_cliente)
    return Cliente(**novo_cliente)