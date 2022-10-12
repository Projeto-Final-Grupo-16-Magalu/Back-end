from typing import Optional
from games.modelos.produto import AtualizacaoProduto, Produto
from games.servidor.database import obter_colecao
from games.configuracoes import COLECAO_PRODUTOS
from bson import ObjectId

# 1.Cadastrar um produto
async def inserir_novo_produto(produto: dict) -> dict: 
    colecao = obter_colecao(COLECAO_PRODUTOS)
    await colecao.insert_one(produto)
    return produto


# 2.Atualizar os dados de um produto.
async def atualizar_por_codigo(id : str, produto: AtualizacaoProduto) ->bool:
    produto = { K: v for K, v in produto.dict().items() if v is not None}
    
    filtro = {
        '_id':ObjectId(id)
    }
    colecao = obter_colecao(COLECAO_PRODUTOS)

    produto_atualizado = {
        "$set": produto
    }
    alterado = await colecao.update_one(filtro, produto_atualizado)
    return alterado



# 3.Pesquisar um produto.
async def pesquisar_pelo_id_produto(id):
    filtro = {
        '_id' : ObjectId(id)
    }
    colecao = obter_colecao(COLECAO_PRODUTOS)
    produto = await colecao.find_one(filtro)
    return produto


# 4.Pesquisar um produto pelo nome.
async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    colecao = obter_colecao(COLECAO_PRODUTOS)
    produto = await colecao.find_one({'nome' : nome})
    return produto


# 5.Remover um produto.
async def delete_produto(id):
    colecao = obter_colecao(COLECAO_PRODUTOS)
    remover = await colecao.delete_one({'_id' : ObjectId(id)})
    return remover




 #PS:  import pdb; pdb.set_trace()