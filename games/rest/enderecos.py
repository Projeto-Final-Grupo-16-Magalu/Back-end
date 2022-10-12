from typing import List
from fastapi import APIRouter, status

from games.modelos.endereco import Endereco, ErroEnderecoJaCadastrado
import games.regras.enderecos as enderecos_regras
from games.modelos.endereco import Endereco, EnderecosCliente
from games.rest.documentacao import DESCRICAO_CADASTRAR_ENDERECO, DESCRICAO_PESQUISAR_ENDERECO, DESCRICAO_DELETAR_ENDERECO   

# Minha rota API de endereços
rota_enderecos = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/endereços",
    tags = ["Endereços"]
)

# Cadastrar Endereço
@rota_enderecos.post(
    "/{email}",
    summary= "Cadastro de novo endereço",
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
async def inserir_novo_endereco(email: EmailStr, endereco: Endereco):
    novo_endereco = await enderecos_regras.inserir_novo_endereco(endereco, email)
    return novo_endereco

# Pesquisa endereço pelo email.
@rota_enderecos.get(
    "/{email}",
    summary= "Pesquisa de endereço por email",
    description= DESCRICAO_PESQUISAR_ENDERECO,
    status_code=status.HTTP_200_OK,
    response_model = EnderecosCliente
    responses = {
        status.HTTP_404_GONE:{
            "description": "Endereço não encontrado",
            "model": ErroEnderecoNaoEncontrado}    
        }
    }
)
async def pesquisar_endereco_por_email(email: Emailstr):
    enderecos = await enderecos_regras.pesquisar_endereco_por_email(email)
    return enderecos

#Deleta endereço pelo id.
@rota_enderecos.delete(
    "/{email}{id_endereco}",
    summary= "Deletar endereço do cliente pelo id do endereço",
    description= DESCRICAO_DELETAR_ENDERECO,
    status_code=status.HTTP_200_OK,
    response_model = EnderecosCliente
    responses = {
        status.HTTP_410_GONE:{
            "description": "Esse endereço já foi removido para esse usuário",
            "model": ErroEnderecoJaRemovido}
        status.HTTP_404_GONE:{
            "description": "Endereço não encontrado",
            "model": ErroEnderecoNaoEncontrado
    }
)
async def remover_endereco_do_cliente_por_id(email: Emailstr, id_endereco: _id):
    enderecos = await enderecos_regras.remover_endereco_do_cliente_por_id(email, id_endereco)
    return enderecos
