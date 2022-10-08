from typing import List
from fastapi import APIRouter, status
from games.modelos.endereco import Endereco, ErroEnderecoJaCadastrado
import games.regras.enderecos as enderecos_regras
from games.modelos.endereco import Endereco, EnderecosCliente
from games.rest.documentacao import DESCRICAO_CADASTRAR_ENDERECO, DESCRICAO_PESQUISAR_ENDERECO   

# Minha rota API de endereços
rota_enderecos = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/endereços",
    tags = ["Endereços"]
)

# Cadastrar Endereço
@rota_enderecos.post(
    "/{email}",
    summary= "Cadastro de endereço",
    description= DESCRICAO_CADASTRAR_ENDERECO,
    status_code=status.HTTP_201_CREATED,
    response_model= Endereco, 
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Esse endereço já foi cadastrado para esse usuário",
            "model": ErroEnderecoJaCadastrado
        }
    }
)
async def inserir_novo_endereco(endereco: Endereco):
    novo_endereco = await enderecos_regras.inserir_novo_endereco(endereco)
    return novo_endereco

# Pesquisa endereço pelo email.
@rota_enderecos.get(
    "/{email}",
    summary= "Pesquisa de endereço",
    description= DESCRICAO_PESQUISAR_ENDERECO,
    status_code=status.HTTP_201_CREATED,
    response_model= Endereco, 
    responses = {
        status.HTTP_409_CONFLICT:{
            "description": "Esse endereço já foi cadastrado para esse usuário",
            "model": ErroEnderecoJaCadastrado
        }
    }
    response_model = EnderecosCliente
)
async def pesquisar_endereco_por_email(email: str):
    enderecos = await enderecos_regras.pesquisar_endereco_pelo_email(email)
    return enderecos
