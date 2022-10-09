from games.configuracoes import COLECAO_CARRINHOS
from games.servidor.database import obter_colecao

from games.modelos.carrinho import Carrinho


async def cria_carrinho(carrinho: Carrinho):
    try:
        colecao = obter_colecao(COLECAO_CARRINHOS)
        await colecao.insert_one(carrinho.dict())
        return carrinho
    except Exception as e:
        print(f'cria_carrinho.erro: {e}')

async def pesquisa_carrinhos(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email
        }
        carrinhos = await obter_colecao(COLECAO_CARRINHOS).find(filtro)
        return carrinhos
    except Exception as e:
        print(f'pesquisa_carrinhos.erro: {e}')


async def pesquisa_carrinho_aberto_cliente(cliente_email):
    try:
        filtro = {
            "cliente": cliente_email,
            "aberto": True
        }
        carrinho = await obter_colecao(COLECAO_CARRINHOS).find_one(filtro)
        print(f'PERSISTÊNCIA: pesquisa_carrinho_aberto_cliente: {carrinho}')
        return carrinho
    except Exception as e:
        print(f'pesquisa_carrinho_aberto_cliente.erro: {e}')

async def pesquisa_carrinhos_fechado_cliente(email_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_carrinhos_fechado_cliente.erro: {e}')

async def pesquisa_carrinhos(skip=1, limit=10):
    try:
        ## Realiza busca paginada de todos os carrinhos cadastros no banco
        cursor = obter_colecao(COLECAO_CARRINHOS).find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        return clientes

    except Exception as e:
        print(f'pesquisa_carrinhos.erro: {e}')

async def pesquisa_produto_carrinho(id_produto):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_produto_carrinho.erro: {e}')

async def atualiza_carrinho(id_carrinho, dados_carrinho):
    try:
        ...

    except Exception as e:
        print(f'atualiza_carrinho.erro: {e}')


async def cria_item_carrinho(id_carrinho, codigo_produto):
    try:
        ...

    except Exception as e:
        print(f'cria_item_carrinho.erro: {e}')

async def atualiza_item_carrinho(id_carrinho, codigo_produto):
    try:
        ...

    except Exception as e:
        print(f'atualiza_item_carrinho.erro: {e}')


async def fecha_carrinho(id_carrinho):
    try:
        ...

    except Exception as e:
        print(f'fecha_carrinho.erro: {e}')

async def deleta_carrinho(id_carrinho):
    try:
        ...

    except Exception as e:
        print(f'deleta_carrinho.erro: {e}')
