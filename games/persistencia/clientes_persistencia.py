"""
Módulo responsável pela persistência dos clientes.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar os clientes no MongoDB.
"""

#****** checar nome de persistencia do banco de dados****
from typing import List, Optional

from database.py import connect_db
from database.py import disconnect_db

class Clientes:
    # Nome do cliente
    NOME = "nome"
    # Campo email do cliente
    EMAIL = "email"
   

# Deixando o meu 'recurso de conversa' com coleção global.
COLECAO_CLIENTES = connect_db("clientes")
COLECAO_CLIENTES = disconnect_db("clientes")

async def pesquisar_pelo_email(email_cliente: str) -> Optional[dict]:
    # Filtro para a pesquisa por e-mail
    filtro = {
        Clientes.EMAIL: email_cliente
    }
    # Consultando no banco dados o primeiro cliente
    # que contenha o email informado.
    clientes = await COLECAO_CLIENTES.find_one(filtro)

    return clientes

async def pesquisar_todos() -> List[dict]:
    # Filtro vazio, desejo todos os clientes
    filtro = {}
    # Obtendo um 'cursor' para varrer todos os clientes
    cursor_pesquisa = COLECAO_CLIENTES.find(filtro)
    # Varrendo todas os clientes e 'colocando-os' 
    # dentro de uma lista.
    lista_todos = [
        clientes
        async for clientes in cursor_pesquisa
    ]

    return lista_todos

async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    # Filtro para a pesquisa
    filtro = {
        Clientes.NOME: nome
    }
    # Consultando no banco dados o primeiro nome
    # que contenha o código informado.
    clientes = await COLECAO_CLIENTES.find_one(filtro)

    return clientes

#********************REVISAR****************************

async def inserir_um_novo_cliente(novo_cliente: dict) -> dict:
    # Não validaremos aqui. Mais detalhes veja a 
    # sessão do 'Cadastro da nova música no MongoDB'
    # no arquivo README.md
    await COLECAO_CLIENTES.insert_one(novo_cliente)
    # O registro `nova_cliente` recebe o atributo '_id'
    # que é a chave no banco de dados MongoDB.
    return novo_cliente