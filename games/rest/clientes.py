from fastapi import APIRouter

rota_clientes = APIRouter(prefix="/api/clientes")

@rota_clientes.post("/")
def criar_cliente(cliente: dict):
    pass

@rota_clientes.put("/{codigo_cliente}")
def atualizar_cliente(codigo_cliente: str, cliente: dict):
    pass
    
@rota_clientes.delete("/{codigo_cliente}")
def remover_cliente(codigo_cliente: str):
    pass

@rota_clientes.get("/{codigo_cliente}")
def pesquisar_cliente(codigo_cliente: str):
    pass
    
@rota_clientes.get("/")
def pesquisar_todos_clientes():
    pass