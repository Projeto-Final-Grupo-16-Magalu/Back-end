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

    print(f'REGRAS: criar_novo_carrinho: {cliente}')

    # Caso o cliente não seja encontrado, lança exceção
    if cliente == None:
        raise NaoEncontradoExcecao('Cliente não cadastrado.')

    # Caso o cliente exista, valida se já existe carrinho aberto para esse cliente
    await validar_novo_carrinho(carrinho.cliente)

    # Caso a validação acima seja atendida, criar novo carrinho
    await carrinho_persistencia.cria_carrinho(carrinho)
    print(f'REGRAS: criar_novo_carrinho: {carrinho}')
    return carrinho

async def pesquisar_por_todos_carrinhos() -> List[dict]:
    todos_carrinhos = await carrinho_persistencia.pesquisa_carrinhos()
    if not todos_carrinhos:
        raise NaoEncontradoExcecao('Não há nenhum carrinho cadastrado.')
    return todos_carrinhos

async def validar_novo_carrinho(email_cliente: EmailStr):
    outro_carrinho = await carrinho_persistencia.pesquisa_carrinho_aberto_cliente(email_cliente)
    if outro_carrinho != None:
        raise OutroRegistroExcecao('Já existe um carrinho aberto para este cliente')

async def produto_existe_no_carrinho(carrinho: Carrinho, novo_produto: Produto):
    item_carrinho = await carrinho_persistencia.pesquisa_produto_carrinho(novo_produto.codigo)
    if not item_carrinho:
        return await carrinho_persistencia.cria_item_carrinho(carrinho, novo_produto)
    if novo_produto in item_carrinho:
        return await carrinho_persistencia.atualiza_item_carrinho(carrinho, novo_produto)
    raise NaoEncontradoExcecao("Produto inexistente")
