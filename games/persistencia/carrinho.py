from games.configuracoes import COLECAO_CARRINHOS, COLECAO_PRODUTOS
from games.logs import logger
from games.modelos.carrinho import Carrinho
from games.servidor.database import obter_colecao


colecao = obter_colecao(COLECAO_CARRINHOS)


async def cria_carrinho(carrinho: Carrinho):
    try:
        retorno_insercao = await colecao.insert_one(carrinho.dict())
        if retorno_insercao.acknowledged:
            carrinho = await pesquisa_carrinho_pelo_codigo(retorno_insercao.inserted_id)
            return carrinho
        return None
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinhos(email_cliente):
    try:
        filtro = {
            'cliente': email_cliente
        }
        carrinhos = await colecao.find(filtro)
        return carrinhos
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinho_aberto_cliente(email_cliente, return_id: bool = True):
    try:
        filtro = {
            'cliente': email_cliente,
            'aberto': True
        }
        if return_id:
            carrinho = await colecao.find_one(filtro)
        else:
            carrinho = await colecao.find_one(filtro, {'_id': 0})
        return carrinho
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinho_pelo_codigo(id_carrinho):
    try:
        filtro = {
            '_id': id_carrinho
        }
        carrinho = await colecao.find_one(filtro, {'_id': 0} )
        return carrinho
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinhos_fechado_cliente(email_cliente, skip=1, limit=100):
    try:
        filtro = {
            'cliente': email_cliente,
            'aberto': False
        }
        cursor = colecao.find(filtro, {'_id': 0}).skip(int(skip)).limit(int(limit))
        carrinhos = await cursor.to_list(length=int(limit))
        return carrinhos
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinhos_fechados(skip=1, limit=100):
    try:
        filtro = {
            'aberto': False
        }
        cursor = colecao.find(filtro, {'_id': 0}).skip(int(skip)).limit(int(limit))
        carrinhos = await cursor.to_list(length=int(limit))
        return carrinhos
    except Exception as e:
        logger.exception(e)


async def pesquisa_carrinhos(skip=1, limit=10):
    try:
        # Realiza busca paginada de todos os carrinhos cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        return clientes

    except Exception as e:
        logger.exception(e)


async def pesquisa_item_carrinho(email_cliente, codigo_produto):
    try:
        filtro = {
            'cliente': email_cliente,
            'produtos': { '$elemMatch': {'produto': codigo_produto}}}
        produto_existente = await colecao.find_one(filtro)
        return produto_existente
    except Exception as e:
        logger.exception(e)


async def cria_item(quantidade: int, codigo: int):
    try:
        filtro = {
            'codigo': codigo
        }
        novo_produto = await obter_colecao(COLECAO_PRODUTOS).find_one(filtro)
        novo_item = {
            'produto': codigo,
            'quantidade': quantidade,
            'valor': quantidade * novo_produto['preco']
            }
        return novo_item

    except Exception as e:
        logger.exception(e)


async def cria_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente
        }
        carrinho = await pesquisa_carrinho_aberto_cliente(email_cliente)
        novo_item = await cria_item(quantidade, codigo_produto)
        atualizacao_carrinho = {'$set': {
            'quantidade_produtos':
                int(carrinho['quantidade_produtos']) + quantidade,
            'valor_total':
                float(carrinho['valor_total']) + float(novo_item['valor']*quantidade)
        },
            '$push': {
                'produtos': novo_item
            }}
        await colecao.update_many(filtro, atualizacao_carrinho)
        carrinho_atualizado = await pesquisa_carrinho_pelo_codigo(carrinho['_id'])
        return carrinho_atualizado

    except Exception as e:
        logger.exception(e)


async def atualiza_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente,
            'aberto': True,
            'produtos': {'$elemMatch': {'produto': codigo_produto}}
        }
        carrinho = await colecao.find_one(filtro)
        atualizacao = {'$set': {
            'produtos.$.quantidade':
                carrinho['produtos'][0]['quantidade'] + quantidade,
            'produtos.$.valor':
                carrinho['produtos'][0]['valor'] * carrinho['produtos'][0]['quantidade']
        }}
        await colecao.update_one(filtro, atualizacao, upsert=True)

        carrinho_atualizado = await pesquisa_carrinho_pelo_codigo(carrinho['_id'])
        return carrinho_atualizado

    except Exception as e:
        logger.exception(e)


async def remove_item_carrinho(email_cliente: str, codigo_produto: int):
    try:
        filtro = {
            'cliente': email_cliente,
            'aberto': True,

        }
        atualizacao = {
            '$pull':{
            'produtos':{'produto': codigo_produto}
        }}
        await colecao.update_one(filtro, atualizacao)
        carrinho_atualizado = await pesquisa_carrinho_aberto_cliente(email_cliente, False)
        logger.info(f'carrinho_atualizado={carrinho_atualizado}')
        return carrinho_atualizado

    except Exception as e:
        logger.exception(e)


async def fecha_carrinho(id_carrinho, endereco_entrega):
    try:
        dados = {
            'aberto': False,
            'entrega': endereco_entrega
        }

        atualizacao = await colecao.update_one(
            {'_id': id_carrinho},
            {'$set': dados}
        )

        if atualizacao.modified_count:
            carrinho_atualizado = await pesquisa_carrinho_pelo_codigo(id_carrinho)
            return carrinho_atualizado

        return None

    except Exception as e:
        logger.exception(e)
