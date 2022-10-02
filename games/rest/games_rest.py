from fastapi import APIRouter

rota_games = APIRouter(
    prefix="/api/games"
)


@rota_games.post("/")
def criar_novo_produto(produto: dict):
    print("Salvar novo produto", produto)
    return{
    "codigo" : "texto"
    }

@rota_games.put("/{codigo_produto}")
def atualizar_produto(codigo_produto: str, produto: dict):
    print("Atualizar produto", codigo_produto, "|", produto)
    return None
    
@rota_games.delete("/{codigo_produto}")
def remover_produto(codigo_produto: str):
    print("Remover produto", codigo_produto)
    return None

@rota_games.get("/{codigo_produto}")
def pesquisar_produto(codigo_produto: str):
    print("Pesquisar produto pelo codigo", codigo_produto)
    return {
        "codigo": codigo_produto,
        "nome": "Lavadora de Roupas Consul 9kg - 15 Programas de Lavagem Branca CWB09 ABANA",
        "descricao": "A lavadora de roupas Consul CWB09AB conta com funções que irão facilitar o seu dia a dia. Com ela, você economiza até 70% de sabão em pó. Com 9Kg de capacidade de roupa seca, tem cesto de plástico e 15 programas de lavagem como: Dosagem Extra Fácil: onde as roupas ficam bem lavadas e ainda tem uma economia de até 70% de sabão em pó.",
        "preco": 20,
        "quantidade": 5
        
    }
    
@rota_games.get("/")
def pesquisar_todos_produto():
    print("Pesquisar todos produtos")
    return [{
        "codigo": 123,
        "nome": "Lavadora de Roupas Consul 9kg - 15 Programas de Lavagem Branca CWB09 ABANA",
        "descricao": "A lavadora de roupas Consul CWB09AB conta com funções que irão facilitar o seu dia a dia. Com ela, você economiza até 70% de sabão em pó. Com 9Kg de capacidade de roupa seca, tem cesto de plástico e 15 programas de lavagem como: Dosagem Extra Fácil: onde as roupas ficam bem lavadas e ainda tem uma economia de até 70% de sabão em pó.",
        "preco": 20,
        "quantidade": 5
    }]