from fastapi import HTTPException
from pydantic import EmailStr
from typing import List

from games.logs import logger
from games.modelos.carrinho import Carrinho, ItemCarrinho, AbrirCarrinho
from games.modelos.produto import Produto

import games.persistencia.carrinho as carrinho_persistencia
import games.persistencia.clientes as clientes_persistencia
import games.persistencia.enderecos as enderecos_persistencia
import games.persistencia.produtos as produtos_persistencia


async def criar_novo_carrinho(carrinho: AbrirCarrinho) -> Carrinho:
    # Busca cliente com e-mail informado no carrinho
    cliente = await clientes_persistencia.pesquisar_pelo_email(carrinho.cliente)
    logger.info(f'email_cliente={carrinho.cliente} - cliente={cliente}')
    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        # Not found
        raise HTTPException(status_code=404, detail=f'Cliente não encontrado')
    # Caso o cliente exista, valida se já existe carrinho aberto para esse cliente
    await verifica_carrinho_aberto(carrinho.cliente)
    # Caso a validação acima seja atendida, criar novo carrinho
    await carrinho_persistencia.cria_carrinho(Carrinho(cliente=carrinho.cliente))
    logger.info(f'carrinho={carrinho}')
    return carrinho


# Verifica se há produtos no estoque suficiente para o carrinho e atualiza o estoque
async def verifica_quantidade_produto(item_carrinho: ItemCarrinho, produto: Produto):
    if produto['quantidade_em_estoque'] < item_carrinho.quantidade:
        logger.warning(f'Estoque insuficiente - produto={produto}')
        # Precondition failed
        raise HTTPException(status_code=412, detail=f'Estoque insuficiente')
    await produtos_persistencia.atualiza_produto(produto['codigo'], item_carrinho.quantidade)


# Adiciona item ao carrinho já existente
async def adiciona_item_carrinho(email: str, item_carrinho: ItemCarrinho):
    logger.info(f'cliente={email} : item={item_carrinho}')
    # Busca produto pelo código
    produto = await produtos_persistencia.pesquisar_pelo_codigo(item_carrinho.produto)
    await verifica_quantidade_produto(item_carrinho, produto)
    carrinho_atualizado = await item_no_carrinho(email, item_carrinho.produto, item_carrinho.quantidade)
    logger.info(f'carrinho={carrinho_atualizado}')
    return carrinho_atualizado


# Pesquisa todos os carrinhos
async def pesquisar_por_todos_carrinhos() -> List[dict]:
    todos_carrinhos = await carrinho_persistencia.pesquisa_carrinhos()
    if not todos_carrinhos:
        logger.warning('Não há carrinho cadastrado')
        # Not found
        raise HTTPException(status_code=404, detail=f'Carrinho não encontrado')
    return todos_carrinhos


# Verifica se o cliente tem carrinho aberto
async def verifica_carrinho_aberto(email_cliente: EmailStr):
    carrinho = await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente)
    # Se o carrinho aberto existe, retorna carrinho
    if carrinho != None:
        return carrinho
    return carrinho


# Verifica se já existe o item no carrinho e atualiza carrinho com o item
async def item_no_carrinho(email_cliente, codigo_produto, quantidade):
    logger.info(f'cliente={email_cliente} - produto={codigo_produto} - quantidade={quantidade}')
    carrinho = await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente, False)
    if carrinho == None:
        logger.warning(f'Não existe carrinho aberto para o cliente={email_cliente}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Não existe carrinho aberto para o cliente')    
    logger.info(f'carrinho={carrinho}')
    # Verifica se já existe o produto no carrinho
    produto_existente = await carrinho_persistencia.pesquisa_item_carrinho(email_cliente, codigo_produto)
    # Se não há item no carrinho:
    if produto_existente == None:
        # Cria item
        carrinho_atualizado = await carrinho_persistencia.cria_item_carrinho(email_cliente, codigo_produto, quantidade)
        return carrinho_atualizado
    # Se há item no carrinho, atualiza item
    carrinho_atualizado = await carrinho_persistencia.atualiza_item_carrinho(email_cliente, codigo_produto, quantidade)
    logger.info(f'carrinho={carrinho_atualizado}')
    return carrinho_atualizado


async def remove_item_carrinho(email_cliente, codigo_produto):
    logger.info(f'cliente={email_cliente} - produto={codigo_produto}')
    await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente)
    # Verifica se já existe o produto no carrinho
    produto_existente = await carrinho_persistencia.pesquisa_item_carrinho(email_cliente, codigo_produto)
    # Se não há item no carrinho:
    if produto_existente == None:
        logger.warning(f'Produto não encontrado={produto_existente}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Produto não encontrado')
    # Se há item no carrinho, remove item
    carrinho_atualizado = await carrinho_persistencia.remove_item_carrinho(email_cliente, codigo_produto)
    logger.info(f'carrinho={carrinho_atualizado}')
    return carrinho_atualizado


# Fecha carrinho do cliente
async def fechar_carrinho(email_cliente: EmailStr):
    # Verifica se e-mail é válido: existe cliente cadastrado
    cliente = await clientes_persistencia.pesquisar_pelo_email(email_cliente)
    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        logger.warning(f'Cliente não cadastrado={email_cliente}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Cliente não cadastrado')
    # Caso o cliente exista, verifica se já existe carrinho aberto para esse cliente
    carrinho = await verifica_carrinho_aberto(email_cliente)
    # pesquisar_endereco_entrega
    endereco_entrega = await enderecos_persistencia.pesquisar_endereco_entrega(email_cliente)
    # Fecha carrinho
    carrinho = await carrinho_persistencia.fecha_carrinho(carrinho['_id'], endereco_entrega)
    logger.info(f'carrinho={carrinho}')
    # Retorna carrinho atualizado
    return carrinho


# Pesquisa carrinho abertos de um cliente
async def pesquisar_carrinho_aberto_cliente(email_cliente: EmailStr):
    carrinho = await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente, False)
    if carrinho == None:
        logger.warning(f'Não existe carrinho aberto para o cliente={email_cliente}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Não existe carrinho aberto para o cliente')
    logger.info(f'cliente={email_cliente} : carrinho={carrinho}')
    return carrinho


# Pesquisa carrinhos fechados de um cliente
async def pesquisar_carrinhos_fechados_cliente(email_cliente: EmailStr):
    carrinhos = await carrinho_persistencia.pesquisa_carrinhos_fechado_cliente(email_cliente)
    if carrinhos == None:
        logger.warning(f'Não existem carrinhos fechados para o cliente={email_cliente}')
        # Not found
        raise HTTPException(status_code=404, detail=f'Não existem carrinhos fechados para o cliente')
    logger.info(f'cliente={email_cliente} : carrinhos={carrinhos}')
    return carrinhos


# Pesquisa carrinhos fechados
async def pesquisar_carrinhos_fechados(quantidade: int):
    carrinhos = await carrinho_persistencia.pesquisa_carrinhos_fechados(limit=quantidade)
    if carrinhos == None:
        logger.warning(f'Não existem carrinhos fechados')
        # Not found
        raise HTTPException(status_code=404, detail=f'Não existem carrinhos fechados')
    logger.info(f'carrinhos={carrinhos}')
    return carrinhos