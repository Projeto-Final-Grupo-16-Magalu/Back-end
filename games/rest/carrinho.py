from fastapi import APIRouter
from pydantic import EmailStr

import games.regras.carrinho as carrinho_regras
from games.modelos.carrinho import Carrinho, ItemCarrinho


rota_carrinho = APIRouter(
    prefix="/api/carrinho-compras"
)

# Cria um carrinho de compras aberto
@rota_carrinho.post(
    "/",
    response_model = Carrinho
    )
async def criar_novo_carrinho(carrinho: Carrinho):
    carrinho_criado = await carrinho_regras.criar_novo_carrinho(carrinho)
    return carrinho_criado

# Atualiza quantidade de itens do carrinho
@rota_carrinho.put(
    "/adicionar_item",
    response_model = Carrinho
    )
async def adicionar_item_carrinho(email_cliente: str, item_carrinho: ItemCarrinho):
    carrinho_atualizado = await carrinho_regras.adiciona_item_carrinho(email_cliente, item_carrinho)
    return carrinho_atualizado


# Fecha um carrinho aberto
@rota_carrinho.put("/fechar/{email_cliente}")
async def fechar_carrinho(email_cliente: EmailStr):
    status_carrinho = await carrinho_regras.fechar_carrinho(email_cliente)
    return status_carrinho

# Remove um carrinho (Opcional)
@rota_carrinho.delete("/{email_cliente}")
async def remover_carrinho(email_cliente: EmailStr):
    return(f'remover_carrinho {email_cliente}')

# Consulta carrinho de compras aberto de um cliente
@rota_carrinho.get("/{email_cliente}")
async def pesquisar_carrinho(email_cliente: EmailStr):
    return(f'pesquisar_carrinho: cliente: {email_cliente}')

# Consulta os carrinhos de compra fechados de um cliente (Opcional)
# Consulta os produtos e suas quantidades em carrinhos fechados (Opcional)
# Consulta quantos carrinhos fechados os clientes possuem (Opcional)
@rota_carrinho.get("/fechados/{email_cliente}")
async def pesquisar_carrinhos_fechados(email_cliente: EmailStr):
    return(f'pesquisar_carrinhos_fechados: cliente: {email_cliente}')