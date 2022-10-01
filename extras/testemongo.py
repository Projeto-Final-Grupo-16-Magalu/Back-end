from motor.motor_asyncio import AsyncIOMotorClient

async def testar():
    url = "mongodb+srv://CarolineMelo:<C4r0l1n3>@luizacode.potbfvk.mongodb.net/gamesbd??retryWrites=true&w=majority"
    cliente_mongo = AsyncIOMotorClient(url)

    bd = cliente_mongo.get_default_database()

    colecao_teste01 = bd["teste01"]

    await colecao_teste01.insert_one({
        "teste": "Carol",
        "codigo":1
    })
    print("Pronto!")

    if __name__=="__main__":
        import asyncio
        asyncio.run(testar_atlas())