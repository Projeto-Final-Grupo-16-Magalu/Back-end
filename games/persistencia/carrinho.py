async def cria_carrinho(colecao, carrinho):
    try:
        ...

    except Exception as e:
        print(f'cria_carrinho.erro: {e}')

async def pesquisa_carrinho(colecao, id_carrinho):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_carrinho.erro: {e}')

async def pesquisa_carrinho_aberto_cliente(colecao, email_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_carrinho_aberto_cliente.erro: {e}')

async def pesquisa_carrinhos_fechado_cliente(colecao, email_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_carrinhos_fechado_cliente.erro: {e}')

async def pesquisa_carrinhos(colecao, skip, limit):
    try:
        ## Realiza busca paginada de todos os carrinhos cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        return clientes

    except Exception as e:
        print(f'pesquisa_carrinhos.erro: {e}')

async def atualiza_carrinho(colecao, id_carrinho, dados_carrinho):
    try:
        ...

    except Exception as e:
        print(f'atualiza_carrinho.erro: {e}')

async def fecha_carrinho(colecao, id_carrinho):
    try:
        ...

    except Exception as e:
        print(f'fecha_carrinho.erro: {e}')

async def deleta_carrinho(colecao, id_carrinho):
    try:
        ...

    except Exception as e:
        print(f'deleta_carrinho.erro: {e}')
