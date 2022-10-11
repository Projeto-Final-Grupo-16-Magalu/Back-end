from pydantic import EmailStr
from games.configuracoes import COLECAO_CARRINHOS, COLECAO_PRODUTOS
from games.servidor.database import obter_colecao

from games.modelos.carrinho import Carrinho


colecao = obter_colecao(COLECAO_CARRINHOS)

async def cria_carrinho(carrinho: Carrinho):
    try:
        await colecao.insert_one(carrinho.dict())
        return carrinho
    except Exception as e:
        print(f'cria_carrinho.erro: {e}')

async def pesquisa_carrinhos(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email
        }
        carrinhos = await colecao.find(filtro)
        return carrinhos
    except Exception as e:
        print(f'pesquisa_carrinhos.erro: {e}')


async def pesquisa_carrinho_aberto_cliente(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email,
            "aberto": True
        }
        carrinho = await colecao.find_one(filtro)
        return carrinho
    except Exception as e:
        print(f'pesquisa_carrinho_aberto_cliente.erro: {e}')

async def pesquisa_carrinho_pelo_codigo(id_carrinho):
    try:
        filtro = {
            "_id": id_carrinho
        }
        carrinho = await colecao.find_one(filtro)
        return carrinho
    except Exception as e:
        print(f'pesquisa_carrinho_pelo_codigo.erro: {e}')

async def pesquisa_carrinhos_fechado_cliente(email_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_carrinhos_fechado_cliente.erro: {e}')

async def pesquisa_carrinhos(skip=1, limit=10):
    try:
        ## Realiza busca paginada de todos os carrinhos cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        return clientes

    except Exception as e:
        print(f'pesquisa_carrinhos.erro: {e}')


async def pesquisa_item_carrinho(email_cliente, codigo_produto):
    try:
        filtro = {
            'cliente': email_cliente,
            'produtos': [{
                'produto': codigo_produto
        }]
        }
        produto_existente = await colecao.find_one(filtro)
        return produto_existente #PQ None?!?!?!?! :'(
    except Exception as e:
        print(f'pesquisa_item_carrinho.erro: {e}')


async def cria_item(quantidade: int, codigo: int):
    try:
        filtro = {
            "codigo": codigo
        }
        novo_produto = await obter_colecao(COLECAO_PRODUTOS).find_one(filtro)
        novo_item = {
            'produto': codigo,
            'quantidade': quantidade,
            'valor': quantidade * novo_produto['preco']
            }
        return novo_item

    except Exception as e:
        print(f'cria_item.erro: {e}')


async def cria_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente
        }
        carrinho = await colecao.find_one(filtro)
        novo_item = await cria_item(quantidade, codigo_produto)
        atualizacao_carrinho = {'$set': {
            'quantidade_produtos': int(carrinho['quantidade_produtos']) + quantidade,
            'valor_total': float(carrinho['valor_total']) + float(novo_item['valor'])
        },
            '$push': {
                'produtos': novo_item
            }}
        await colecao.update_many(filtro, atualizacao_carrinho)
        return carrinho

    except Exception as e:
        print(f'cria_item_carrinho.erro: {e}')

async def atualiza_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente,
            'produtos': {'produto': codigo_produto}
        }
        carrinho = await colecao.find_one(filtro)
        atualizacao = {'$set': {'produtos': [{
            'quantidade': carrinho['quantidade'] + quantidade,
            'valor_total': carrinho['valor_total'] * quantidade
        }]}
            }
        await colecao.update_one(filtro, atualizacao)
        return carrinho

    except Exception as e:
        print(f'atualiza_item_carrinho.erro: {e}')


async def fecha_carrinho(id_carrinho):
    try:
        dados = {
            "aberto": False
        }

        atualizacao = await colecao.update_one(
            {'_id': id_carrinho},
            {'$set': dados}
        )

        if atualizacao.modified_count:
            return {"message": "Carrinho fechado com sucesso"}

        return None

    except Exception as e:
        print(f'fecha_carrinho.erro: {e}')

async def deleta_carrinho(id_carrinho):
    try:
        ...

    except Exception as e:
        print(f'deleta_carrinho.erro: {e}')
