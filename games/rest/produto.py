from fastapi import APIRouter
from games.modelos.produto import Produto
from games.persistencia.produto import cria_produto


rota_produto = APIRouter(
    prefix="/api/produto"
)


@rota_produto.post("/",response_model=Produto)
async def criar_novo_produto(produto_payload: dict):
    id_produto = await cria_produto(produto_payload)
    print("Salvar novo produto", produto_payload)
    print(id_produto)
    return produto_payload
   
 

@rota_produto.put("/{codigo_produto}")
def atualizar_produto(codigo_produto: str, produto: dict):
    print("Atualizar produto", codigo_produto, "|", produto)
    return None
    
@rota_produto.delete("/{codigo_produto}")
def remover_produto(codigo_produto: str):
    print("Remover produto", codigo_produto)
    return None

@rota_produto.get("/{codigo_produto}")
def pesquisar_produto(codigo_produto: str):
    print("Pesquisar produto pelo codigo", codigo_produto)
    return {
        "codigo": codigo_produto,
        "nome": "Lavadora de Roupas Consul 9kg - 15 Programas de Lavagem Branca CWB09 ABANA",
        "descricao": "A lavadora de roupas Consul CWB09AB conta com funções que irão facilitar o seu dia a dia. Com ela, você economiza até 70% de sabão em pó. Com 9Kg de capacidade de roupa seca, tem cesto de plástico e 15 programas de lavagem como: Dosagem Extra Fácil: onde as roupas ficam bem lavadas e ainda tem uma economia de até 70% de sabão em pó.",
        "preco": 20,
        "quantidade": 5,
        "imagem": str
        
    }
    
@rota_produto.get("/")
def pesquisar_todos_produto():
    print("Pesquisar todos produtos")
    return [{
       
    }]

# @rota_produto.delete("/{codigo_produto}")
# def remover_produto(codigo_produto: str):
#    res = await  remover_uma_produto_pelo_codigo(codigo_produto)
#    print("Remover produto", codigo_produto)
#    return None


     

      
        