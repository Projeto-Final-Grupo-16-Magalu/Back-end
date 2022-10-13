
from typing import List, Optional
from uuid import uuid4
from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
import games.persistencia.enderecos as enderecos_persistencia
from games.modelos.endereco import Endereco, EnderecosCliente
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.regras.clientes import pesquisar_por_email

# Pesquisar endereços por email
async def pesquisar_enderecos_por_email(email: EmailStr, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
    endereco = await enderecos_persistencia.pesquisar_endereço_por_email(email)
    
    # Caso endereço não seja encontrado, lança exceção
    if not endereco and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Endereço não encontrado")
    return endereco

# Validar se o endereço enviado não está cadastrado
async def validar_novo_endereco(endereco:Endereco, email: EmailStr):
    outro_endereco = await enderecos_persistencia.pesquisar_endereços(endereco)
    
    #Caso endereço já tenha sido cadastrado, lança exceção
    if outro_endereco is not None:
            raise OutroRegistroExcecao('Esse endereço já foi cadastrado')
    return outro_endereco
        
# Inserir novo endereço
async def inserir_novo_endereco(endereco: Endereco) -> Endereco:
        # Validar se o endereço enviado não está cadastrado
        await validar_novo_endereco(endereco)
        
        #Caso endereço não estiver cadastrado, cadastrá-lo
        outro_endereco = endereco.dict()
        await enderecos_persistencia.inserir_novo_endereco(outro_endereco)
        return endereco

# Cadastrar um novo endereço para a lista de endereços do cliente
async def cadastrar_novo_endereco_para_cliente(email: EmailStr, endereco: Endereco)
    # Pesquisar se o cliente existe
    cliente = await clientes_persistencia.pesquisar_por_email(email)
    
        # Se o cliente não existe, lança exceção
        if cliente == None:
            raise NaoEncontradoExcecao('Cliente não cadastrado.')
        
        # Se o cliente existe, pesquisar a lista de endereços desse cliente
        novo_endereco = await enderecos_persistencia.pesquisar_enderecos_do_cliente(email)
            
        #Se o novo endereço não estiver na lista, cadastrá-lo
        if not novo_endereco:
            return await enderecos_persistencia.cadastrar_novo_endereco(endereco)
        
        # Se o novo endereço já estiver na lista, lança exceção
        if endereco in novo_endereco:
            raise OutroRegistroExcecao('Esse endereço já foi cadastrado para esse cliente')

# Remover endereço do cliente por id (Opcional)
async def remover_endereco_do_cliente_por_id(email: Emailstr, id_endereco: _id):
    # Pesquisar endereços do cliente pelo email
    endereco_deletar = await enderecos_persistencia.pesquisar_endereco_por_email(email, id_endereco)
    
    # Se o id_endereco estiver na lista, removê-lo
    if id_endereco in endereco_deletar:
        return await enderecos_persistencia.remover_endereco_do_cliente_por_id(email, id_endereco)
    
    #Se o id_endereco não estiver na lista, lança exceção
    raise NaoEncontradoExcecao('Endereço não cadastrado para esse cliente.')