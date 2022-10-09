from typing import List

from pydantic import EmailStr

import games.persistencia.clientes as clientes_persistencia
import games.persistencia.carrinho as carrinho_persistencia
from games.modelos.carrinho import Carrinho
from games.modelos.produto import Produto
from games.regras.excecoes import NaoEncontradoExcecao, OutroRegistroExcecao


async def criar_novo_carrinho(carrinho: Carrinho) -> Carrinho:
    # Busca cliente com e-mail informado no carrinho
    cliente = await clientes_persistencia.pesquisar_pelo_email(carrinho.cliente)

    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        raise NaoEncontradoExcecao('Cliente não cadastrado.')

    # Caso o cliente exista, valida se já existe carrinho aberto para esse cliente
    await verifica_carrinho_aberto(carrinho.cliente)

    # Caso a validação acima seja atendida, criar novo carrinho
    await carrinho_persistencia.cria_carrinho(carrinho)

    return carrinho

async def pesquisar_por_todos_carrinhos() -> List[dict]:
    todos_carrinhos = await carrinho_persistencia.pesquisa_carrinhos()
    if not todos_carrinhos:
        raise NaoEncontradoExcecao('Não há nenhum carrinho cadastrado.')
    return todos_carrinhos

async def verifica_carrinho_aberto(email_cliente: EmailStr, lancar_excecao_carrinho_aberto: bool = True):
    carrinho = await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente)
    if carrinho != None and lancar_excecao_carrinho_aberto:
        raise OutroRegistroExcecao('Já existe um carrinho aberto para este cliente')
    return carrinho

async def produto_existe_no_carrinho(carrinho: Carrinho, novo_produto: Produto):
    item_carrinho = await carrinho_persistencia.pesquisa_produto_carrinho(novo_produto.codigo)
    if not item_carrinho:
        return await carrinho_persistencia.cria_item_carrinho(carrinho, novo_produto)
    if novo_produto in item_carrinho:
        return await carrinho_persistencia.atualiza_item_carrinho(carrinho, novo_produto)
    raise NaoEncontradoExcecao("Produto inexistente")

async def fechar_carrinho(email_cliente: EmailStr):
    # Verifica se e-mail é válido: existe cliente cadastrado
    cliente = await clientes_persistencia.pesquisar_pelo_email(email_cliente)

    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        raise NaoEncontradoExcecao('Cliente não cadastrado.')

    # Caso o cliente exista, verifica se já existe carrinho aberto para esse cliente
    carrinho = await verifica_carrinho_aberto(email_cliente, False)

    # Fecha carrinho
    status = await carrinho_persistencia.fecha_carrinho(carrinho['_id'])

    # Retorna carrinho
    return status