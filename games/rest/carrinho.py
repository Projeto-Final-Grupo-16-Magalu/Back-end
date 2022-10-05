from fastapi import APIRouter

rota_carrinho = APIRouter(
    prefix="/api/carrinho-compras"
)

# Cria um carrinho de compras aberto
@rota_carrinho.post("/")
def criar_novo_carrinho(carrinho: dict):
    return (f'criar_novo_carrinho {carrinho}')

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