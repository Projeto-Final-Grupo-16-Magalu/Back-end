"""
Módulo responsável pela persistência dos ENDEREÇOS.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar os enderecos no MongoDB.
"""
#######################################
# BANCO DE DADOS fazer import do bd aqui.
from typing import List, Optional
# from .persistencia_bd import obter_colecao
###########################################
class CampoEndereco: #preciso acrescentar um email aqui pra fazer a busca por e-mail?
    # atributos de endereco
    ID = "id"
    CEP = "cep"
    LOGRADOURO ="logradouro"
    NUMERO ="numero"
    CIDADE = "cidade"  
    ESTADO = "estado"

# # Deixando o meu 'recurso de conversa' com coleção global.
COLECAO_ENDERECOS = obter_colecao("enderecos")#/ ***(fazer import de função do banco de dados e por no lugar de obter_colecao)

async def pesquisar_pelo_id(id_endereco: str) -> Optional[dict]:
    # Filtro para a pesquisa
    filtro = {
        CampoEndereco.ID: id_endereco
    }
    # Consultando no banco dados primeiro endereco
    # que contenha o id informado.
    enderecos = await COLECAO_ENDERECOS.find_one(filtro)

    return enderecos

async def pesquisar_todos() -> List[dict]:
    # Filtro vazio, desejo todos endereços
    filtro = {}
    # Obtendo um 'cursor' para varrer todas os endereços
    cursor_pesquisa = COLECAO_ENDERECOS.find(filtro)
    # Varrendo todos endereços e 'colocando-os' 
    # dentro de uma lista.
    lista_todos = [
        enderecos
        async for enderecos in cursor_pesquisa
    ]

    return lista_todos

async def pesquisar_pelo_email(email: str) -> Optional[dict]:
    # Filtro para a pesquisa
    filtro = {
        CampoEndereco.EMAIL:email
    }
    # Consultando no banco dados primeiro endereço
    # que contenha email informado.
    endereco = await COLECAO_ENDERECOS.find_one(filtro)

    return endereco


async def inserir_um_novo_endereco(novo_endereco: dict) -> dict:
    # Não validaremos aqui. Mais detalhes veja a 
    # sessão do 'Cadastro de novo endereço no MongoDB'
    # no arquivo README.md
    await COLECAO_ENDERECOS.insert_one(novo_endereco)
    # O registro `novo_endereco` recebe o atributo `_id`
    # que é a chave no banco de dados MongoDB.
    return novo_endereco