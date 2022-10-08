from motor.motor_asyncio import AsyncIOMotorClient
from games.servidor import database
from games.servidor.database import connect_db, db, disconnect_db

   
async def cria_produto(produto):
    await connect_db()
    colecao_produtos = db.colecao_produtos
   
    try:
        produto = await colecao_produtos.insert_one(produto)
        
        #if produto.inserted_id:
           # produto = await cria_produto(colecao_produtos, produto.inserted_id)
        await  disconnect_db()   
        return produto.inserted_id

    except Exception as e:
        print(f'cria_produto.erro: {e}')
