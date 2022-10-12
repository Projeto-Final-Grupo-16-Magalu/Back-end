from fastapi import APIRouter, status
from pydantic.networks import EmailStr

from games.modelos.endereco import Endereco, EnderecosCliente
from games.modelos.endereco import (
    ErroEnderecoNaoEncontrado,
    ErroEnderecoJaCadastrado,
    ErroEnderecoJaRemovido
)
from games.rest.documentacao import (
    DESCRICAO_CADASTRAR_ENDERECO,
    DESCRICAO_PESQUISAR_ENDERECO,
    DESCRICAO_DELETAR_ENDERECO
)

import games.regras.enderecos as enderecos_regras


# Minha rota API de endereços
rota_enderecos = APIRouter(
    # Prefixo para o caminho da rota
    prefix='/api/enderecos',
    tags = ['Endereços']
)


# Cadastrar Endereço
@rota_enderecos.post(
    '/{email}',
    summary= 'Cadastro de novo endereço',
    description= DESCRICAO_CADASTRAR_ENDERECO,
    status_code=status.HTTP_201_CREATED,
    response_model= EnderecosCliente,
    responses = {
        status.HTTP_409_CONFLICT:{
            'description': 'Esse endereço já foi cadastrado para esse usuário',
            'model': ErroEnderecoJaCadastrado
        }
    }
)
async def inserir_novo_endereco(email: EmailStr, endereco: Endereco):
    novo_endereco = await enderecos_regras.inserir_novo_endereco(endereco, email)
    return novo_endereco


# Pesquisa endereço pelo email.
@rota_enderecos.get(
    '/{email}',
    summary= 'Pesquisa de endereço por email',
    description= DESCRICAO_PESQUISAR_ENDERECO,
    status_code=status.HTTP_200_OK,
    response_model = EnderecosCliente,
    responses = {
        status.HTTP_404_NOT_FOUND:{
            'description': 'Endereço não encontrado',
            'model': ErroEnderecoNaoEncontrado}
        }
)
async def pesquisar_endereco_por_email(email: EmailStr):
    enderecos = await enderecos_regras.pesquisar_enderecos_por_email(email)
    return enderecos


#Deleta endereço pelo id.
@rota_enderecos.delete(
    '/{email}&{id_endereco}',
    summary= 'Deletar endereço do cliente pelo id do endereço',
    description= DESCRICAO_DELETAR_ENDERECO,
    status_code=status.HTTP_200_OK,
    response_model = EnderecosCliente,
    responses = {
        status.HTTP_410_GONE:{
            'description': 'Esse endereço já foi removido para esse usuário',
            'model': ErroEnderecoJaRemovido},
        status.HTTP_404_NOT_FOUND:{
            'description': 'Endereço não encontrado',
            'model': ErroEnderecoNaoEncontrado
        }
    }
)
async def remover_endereco_do_cliente_por_id(email: EmailStr, id_endereco: str):
    enderecos = await enderecos_regras.remover_endereco_do_cliente_por_id(email, id_endereco)
    return enderecos