from games.configuracoes import COLECAO_CARRINHOS, COLECAO_PRODUTOS
from games.servidor.database import obter_colecao
from games.modelos.carrinho import Carrinho
from games.logs import logger


colecao = obter_colecao(COLECAO_CARRINHOS)

async def criar_carrinho(carrinho: Carrinho):
    try:
        retorno_insercao = await colecao.insert_one(carrinho.dict())
        if retorno_insercao.acknowledged:
            carrinho = await pesquisar_carrinho_pelo_codigo(retorno_insercao.inserted_id)
            return carrinho
        return None
    except Exception as e:
        logger.exception(e)

async def pesquisar_carrinhos(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email
        }
        carrinhos = await colecao.find(filtro)
        logger.info(carrinhos)
        return carrinhos
    except Exception as e:
        logger.exception(e)


async def pesquisar_carrinho_aberto_cliente(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email,
            "aberto": True
        }
        carrinho = await colecao.find_one(filtro)
        logger.info(carrinho)
        return carrinho
    except Exception as e:
        logger.exception(e)

async def pesquisar_carrinho_pelo_codigo(id_carrinho):
    try:
        filtro = {
            "_id": id_carrinho
        }
        carrinho = await colecao.find_one(filtro, {'_id': 0} )
        logger.info(carrinho)
        return carrinho
    except Exception as e:
        logger.exception(e)

async def pesquisar_carrinhos_fechado_cliente(email_cliente):
    try:
        ...
    except Exception as e:
        logger.exception(e)

async def pesquisar_carrinhos(skip=1, limit=10):
    try:
        ## Realiza busca paginada de todos os carrinhos cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        logger.info(clientes)
        return clientes

    except Exception as e:
        logger.exception(e)


async def pesquisar_item_carrinho(email_cliente, codigo_produto):
    try:
        filtro = {
            'cliente': email_cliente,
            'produtos': { '$elemMatch': {'produto': codigo_produto}}}
        produto_existente = await colecao.find_one(filtro)
        logger.info(produto_existente)
        return produto_existente
    except Exception as e:
        logger.exception(e)


async def criar_item(quantidade: int, codigo: int):
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
        logger.exception(e)


async def criar_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente
        }
        carrinho = await pesquisar_carrinho_aberto_cliente(email_cliente)
        novo_item = await criar_item(quantidade, codigo_produto)
        atualizacao_carrinho = {'$set': {
            'quantidade_produtos': int(carrinho['quantidade_produtos']) + quantidade,
            'valor_total': float(carrinho['valor_total']) + float(novo_item['valor']*quantidade)
        },
            '$push': {
                'produtos': novo_item
            }}
        await colecao.update_many(filtro, atualizacao_carrinho)
        carrinho_atualizado = await pesquisar_carrinho_pelo_codigo(carrinho['_id'])
        logger.info(carrinho_atualizado)
        return carrinho_atualizado

    except Exception as e:
        logger.exception(e)

async def atualizar_item_carrinho(email_cliente: str, codigo_produto: int, quantidade: int):
    try:
        filtro = {
            'cliente': email_cliente,
            'aberto': True,
            'produtos': {'$elemMatch': {'produto': codigo_produto}}
        }
        carrinho = await colecao.find_one(filtro)
        logger.info(carrinho)
        atualizacao = {'$set': {
            'produtos.$.quantidade': carrinho['produtos'][0]['quantidade'] + quantidade,
            'produtos.$.valor': carrinho['produtos'][0]['valor'] * carrinho['produtos'][0]['quantidade']
        }}
        await colecao.update_one(filtro, atualizacao, upsert=True)

        carrinho_atualizado = await pesquisar_carrinho_pelo_codigo(carrinho['_id'])
        logger.info(carrinho_atualizado)
        return carrinho_atualizado

    except Exception as e:
        logger.exception(e)


async def fechar_carrinho(id_carrinho):
    try:
        dados = {
            "aberto": False
        }

        atualizacao = await colecao.update_one(
            {'_id': id_carrinho},
            {'$set': dados}
        )
        logger.info(atualizacao)
        if atualizacao.modified_count:
            carrinho_atualizado = await pesquisar_carrinho_pelo_codigo(id_carrinho)
            logger.info(carrinho_atualizado)
            return carrinho_atualizado

        return None

    except Exception as e:
        logger.exception(e)

async def deletar_carrinho(id_carrinho):
    try:
        ...

    except Exception as e:
        logger.exception(e)
