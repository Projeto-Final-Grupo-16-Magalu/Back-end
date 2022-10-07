
from typing import List, Optional
from uuid import uuid4

from pydantic import EmailStr

import games.persistencia.enderecos as enderecos_persistencia
from games.modelos.endereco import (Endereco, EnderecosCliente)
from games.regras.excecoes import (NaoEncontradoExcecao,
                                            OutroRegistroExcecao)


async def pesquisar_endereco_pelo_email(
    email:EmailStr, lanca_excecao_se_nao_encotrado: bool = False
) -> Optional[dict]:
    endereco = await enderecos_persistencia.pesquisar_endereço_por_email(endereco)
    if not endereco and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Endereço não encontrado")
    return endereco


async def inserir_novo_endereco(endereco: Endereco) -> EnderecosCliente:
        novo_endereco = endereco.dict()
        await enderecos_persistencia.inserir_um_novo_endereco(novo_endereco)
        endereco_geral = endereco(**novo_endereco)
        return endereco_geral