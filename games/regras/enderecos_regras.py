"""
Regras e ajustes para enderecos.
"""

from typing import List, Optional
from uuid import uuid4

import games.persistencia.enderecos_persistencia as enderecos_persistencia
from games.modelos.endereco import (Endereco, EnderecosCliente)
from games.regras.regras_excecoes import (NaoEncontradoExcecao,
                                            OutroRegistroExcecao)


async def pesquisar_por_id(
    id: int, lanca_excecao_se_nao_encotrado: bool = False
) -> Optional[dict]:
    endereco = await enderecos_persistencia.pesquisar_pelo_id(id)
    if not endereco and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Endereço não encontrado")
    return endereco


async def pesquisar_por_todos() -> List[dict]:
    todos = await enderecos_persistencia.pesquisar_todos()
    return todos

# *** É necessária a validação? pois podem havar mais pessoas com o mesmo endereço
async def validar_novo_endereco(endereco: Endereco):
#     # Seria bom validarmos aqui se há nome e artista.
#     # Mas como a camada _rest já fez isto para nós, vamos 'confiar'
#     # nela.

#     # Validando se não há outra música com este nome
#     outra_musica = await musicas_persistencia.pesquisar_pelo_nome(musica.nome)
#     if outra_musica is not None:
#         raise OutroRegistroExcecao("Há outra música com este nome")


    async def inserir_novo_endereco(endereco: Endereco) -> EnderecosCliente:
        await validar_novo_endereco(endereco)

    # 'Convertendo' endereco para ser salvo no banco
    novo_endereco = endereco.dict()
    # Gerando novo código com uuidv4
    novo_endereco[enderecos_persistencia.CampoEndereco.ID] = str(uuid4())

    # Salvando no banco de dados
    await enderecos_persistencia.inserir_um_novo_endereco(novo_endereco)

    # Retornando o registro do endereco completo
    endereco_geral = endereco(**novo_endereco)

    return endereco_geral