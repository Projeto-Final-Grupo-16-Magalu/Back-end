
from typing import List, Optional
from uuid import uuid4

import games.persistencia.enderecos as enderecos_persistencia
from games.modelos.endereco import (Endereco, EnderecosCliente)
from games.regras.excecoes import (NaoEncontradoExcecao,
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

async def validar_novo_endereco(endereco: Endereco):
    async def inserir_novo_endereco(endereco: Endereco) -> EnderecosCliente:
        await validar_novo_endereco(endereco)
    novo_endereco = endereco.dict()
    novo_endereco[enderecos_persistencia.Endereco.id_cliente] = str(uuid4())
    await enderecos_persistencia.inserir_um_novo_endereco(novo_endereco)
    endereco_geral = endereco(**novo_endereco)
    return endereco_geral