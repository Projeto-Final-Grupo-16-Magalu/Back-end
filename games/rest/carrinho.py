from fastapi import APIRouter, status

import games.regras.carrinho as carrinho_regras
import games.persistencia.carrinho as persistencia_carrinho
from games.modelos.carrinho import Carrinho
from games.modelos.cliente import Cliente

rota_carrinho = APIRouter(
    prefix="/api/carrinho-compras"
)

# Cria um carrinho de compras aberto
@rota_carrinho.post("/")
async def criar_novo_carrinho(carrinho: Carrinho):
  #  print(carrinho)
    carrinho_criado = await carrinho_regras.criar_novo_carrinho(carrinho)
    return (f'criar_novo_carrinho {carrinho_criado}')

@rota_carrinho.post(
    "/{email_cliente}")
async def criar_carrinho(email_cliente):
    carrinho_criado = await carrinho_regras.criar_novo_carrinho(email_cliente)
    return carrinho_criado

# Atualiza quantidade de itens do carrinho
@rota_carrinho.put("/{codigo_carrinho}")
def atualizar_carinho(codigo_carrinho: int, carrinho: dict):
    return(f'atualizar_carinho {codigo_carrinho} | {carrinho}')

# Fecha um carrinho aberto
@rota_carrinho.put("/fechar/{codigo_carrinho}")
def fechar_carrinho(codigo_carrinho: int):
    return(f'fechar_carrinho {codigo_carrinho}')

# Remove um carrinho (Opcional)
@rota_carrinho.delete("/{codigo_carrinho}")
def remover_carrinho(codigo_carrinho: int):
    return(f'remover_carrinho {codigo_carrinho}')

# Consulta carrinho de compras aberto de um cliente
@rota_carrinho.get("/{email_cliente}")
def pesquisar_carrinho(email_cliente: str):
    return(f'pesquisar_carrinho: cliente: {email_cliente}')

# Consulta os carrinhos de compra fechados de um cliente (Opcional)
# Consulta os produtos e suas quantidades em carrinhos fechados (Opcional)
# Consulta quantos carrinhos fechados os clientes possuem (Opcional)
@rota_carrinho.get("/fechados/{email_cliente}")
def pesquisar_carrinhos_fechados(email_cliente: str):
    return(f'pesquisar_carrinhos_fechados: cliente: {email_cliente}')