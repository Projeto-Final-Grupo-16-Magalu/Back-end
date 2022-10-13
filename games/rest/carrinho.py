from fastapi import APIRouter
from pydantic import EmailStr

from games.modelos.carrinho import AbrirCarrinho, Carrinho, ItemCarrinho

import games.regras.carrinho as carrinho_regras


rota_carrinho = APIRouter(
    prefix='/api/carrinho-compras',
    tags = ['Carrinho']
)


# Cria um carrinho de compras aberto
@rota_carrinho.post(
    '/',
    response_model=Carrinho
    )
async def criar_novo_carrinho(carrinho: AbrirCarrinho):
    carrinho_criado = await carrinho_regras.criar_novo_carrinho(carrinho)
    return carrinho_criado


# Atualiza quantidade de itens do carrinho
@rota_carrinho.put(
    '/adicionar_item'
    )
async def adicionar_produto_ao_carrinho(email_cliente: str, item_carrinho: ItemCarrinho):
    carrinho_atualizado = await carrinho_regras.adiciona_item_carrinho(email_cliente, item_carrinho)
    return carrinho_atualizado


# Remove um item do carrinho
@rota_carrinho.put(
    '/remover_item'
    )
async def remover_produto_do_carrinho(email_cliente: str, codigo_produto: int):
    carrinho_atualizado = await carrinho_regras.remove_item_carrinho(email_cliente, codigo_produto)
    return carrinho_atualizado


# Fecha um carrinho aberto
@rota_carrinho.put('/fechar/{email_cliente}')
async def fechar_carrinho(email_cliente: EmailStr):
    status_carrinho = await carrinho_regras.fechar_carrinho(email_cliente)
    return status_carrinho


# Remove um carrinho (Opcional)
@rota_carrinho.delete('/{email_cliente}')
async def remover_carrinho(email_cliente: EmailStr):
    return(f'remover_carrinho {email_cliente}')


# Consulta carrinho de compras aberto de um cliente
@rota_carrinho.get('/{email_cliente}')
async def pesquisar_carrinho(email_cliente: EmailStr):
    carrinho = await carrinho_regras.pesquisar_carrinho_aberto_cliente(email_cliente)
    return carrinho


# Consulta os carrinhos de compra fechados de um cliente (Opcional)
@rota_carrinho.get('/fechados/{email_cliente}')
async def pesquisar_carrinhos_fechados(email_cliente: EmailStr):
    carrinhos = await carrinho_regras.pesquisar_carrinhos_fechados_cliente(email_cliente)
    return carrinhos


# Consulta os produtos e suas quantidades em carrinhos fechados (Opcional)
@rota_carrinho.get('/fechados/todos/{quantidade}')
async def pesquisar_a_quantidade_de_carrinhos_fechados(quantidade: int):
    carrinhos = await carrinho_regras.pesquisar_carrinhos_fechados(quantidade)
    return carrinhos


# Consulta quantos carrinhos fechados os clientes possuem (Opcional)
@rota_carrinho.get('/fechados/soma/{email_cliente}')
async def pesquisar_a_quantidade_de_carrinhos_fechados_por_cliente(email_cliente: EmailStr):
    carrinhos = await carrinho_regras.pesquisar_carrinhos_fechados_cliente(email_cliente)
    retorno = {
        'cliente': email_cliente,
        'quantidade_carrinhos_fechados': len(carrinhos)
    }
    return retorno