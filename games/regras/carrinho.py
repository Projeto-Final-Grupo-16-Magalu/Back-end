from typing import List
from games.modelos.carrinho import AbrirCarrinho

from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
import games.persistencia.carrinho as carrinho_persistencia
import games.persistencia.produtos as produtos_persistencia
from games.modelos.carrinho import Carrinho, ItemCarrinho
from games.modelos.produto import Produto
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao
from games.logs import logger

# Criar novo carrinho
async def criar_novo_carrinho(carrinho: AbrirCarrinho) -> Carrinho:
    # Busca cliente com e-mail informado no carrinho
    cliente = await clientes_persistencia.pesquisar_pelo_email(carrinho.cliente)
    logger.info(f'email_cliente={carrinho.cliente} - cliente={cliente}')
    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        raise NaoEncontradoExcecao('Cliente não cadastrado.')

    # Caso o cliente exista, valida se já existe carrinho aberto para esse cliente
    await verificar_carrinho_aberto(carrinho.cliente)

    # Caso a validação acima seja atendida, criar novo carrinho
    await carrinho_persistencia.criar_carrinho(Carrinho(cliente=carrinho.cliente))
    logger.info(f'carrinho={carrinho}')
    return carrinho

# Verifica se há produtos no estoque suficiente para o carrinho e atualiza o estoque
async def verificar_quantidade_produto(item_carrinho: ItemCarrinho, produto: Produto):
    if produto['quantidade_em_estoque'] < item_carrinho.quantidade:
        logger.warning(f'Estoque insuficiente - produto={produto}')
        raise OutroRegistroExcecao('Não há produtos suficiente em estoque.')
    await produtos_persistencia.atualizar_produto(produto['codigo'], item_carrinho.quantidade)

# Adiciona item ao carrinho já existente
async def adicionar_item_carrinho(email: str, item_carrinho: ItemCarrinho):
    logger.info(f'cliente={email} - item={item_carrinho}')
    # Busca produto pelo código
    produto = await produtos_persistencia.pesquisar_pelo_codigo(item_carrinho.produto)
    await verificar_quantidade_produto(item_carrinho, produto)
    carrinho_atualizado = await item_no_carrinho(email, item_carrinho.produto, item_carrinho.quantidade)
    logger.info(f'carrinho={carrinho_atualizado}')
    return carrinho_atualizado

# Pesquisa todos os carrinhos
async def pesquisar_por_todos_carrinhos() -> List[dict]:
    todos_carrinhos = await carrinho_persistencia.pesquisa_carrinhos()
    if not todos_carrinhos:
        logger.warning('Não há carrinho cadastrado')
        raise NaoEncontradoExcecao('Não há carrinho cadastrado.')
    return todos_carrinhos

# Verifica se o cliente tem carrinho aberto
async def verificar_carrinho_aberto(email_cliente: EmailStr):
    carrinho = await carrinho_persistencia.pesquisar_carrinho_aberto_cliente(email_cliente)
    # Se o carrinho aberto existe:
    if carrinho != None:
        return carrinho
    carrinho = await carrinho_persistencia.criar_carrinho(email_cliente)
    return carrinho

#Verifica se já existe o item no carrinho e atualiza carrinho com o item
async def item_no_carrinho(email_cliente, codigo_produto, quantidade):
    logger.info(f'cliente={email_cliente} - produto={codigo_produto} - quantidade={quantidade}')
    await carrinho_persistencia.pesquisar_carrinho_aberto_cliente(email_cliente)
    # Verifica se já existe o produto no carrinho
    produto_existente = await carrinho_persistencia.pesquisar_item_carrinho(email_cliente, codigo_produto)
    # Se não há item no carrinho:
    if produto_existente == None:
        # Cria item
        carrinho_atualizado = await carrinho_persistencia.criar_item_carrinho(email_cliente, codigo_produto, quantidade)
        return carrinho_atualizado
    # Se há item no carrinho:
    # Atualiza item
    carrinho_atualizado = await carrinho_persistencia.atualizar_item_carrinho(email_cliente, codigo_produto, quantidade)
    logger.info(f'carrinho={carrinho_atualizado}')
    return carrinho_atualizado


#Fecha carrinho do cliente
async def fechar_carrinho(email_cliente: EmailStr):
    # Verifica se e-mail é válido: existe cliente cadastrado
    cliente = await clientes_persistencia.pesquisar_pelo_email(email_cliente)

    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        logger.warning(f'Cliente não cadastrado={email_cliente}')
        raise NaoEncontradoExcecao('Cliente não cadastrado.')

    # Caso o cliente exista, verifica se já existe carrinho aberto para esse cliente
    carrinho = await verificar_carrinho_aberto(email_cliente)
    #pesquisar_endereco_entrega
    # Fecha carrinho
    carrinho = await carrinho_persistencia.fechar_carrinho(carrinho['_id'])
    logger.info(f'carrinho={carrinho}')
    # Retorna carrinho atualizado
    return carrinho