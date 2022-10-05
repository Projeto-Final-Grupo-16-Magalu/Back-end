async def cria_produto(colecao, produto):
    try:
        ...

    except Exception as e:
        print(f'cria_produto.erro: {e}')

async def pesquisa_produto(colecao, id_produto):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_produto.erro: {e}')

async def pesquisa_produto_pelo_codigo(colecao, codigo_produto):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_produto_pelo_codigo.erro: {e}')

async def pesquisa_produto_pelo_nome(colecao, nome_produto):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_produto_pelo_nome.erro: {e}')

async def pesquisa_produtos(colecao, skip, limit):
    try:
        ## Realiza busca paginada de todos os produtos cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        produtos = await cursor.to_list(length=int(limit))
        return produtos

    except Exception as e:
        print(f'pesquisa_produtos.erro: {e}')

async def atualiza_produto(colecao, id_produto, datos_produto):
    try:
        ...

    except Exception as e:
        print(f'atualiza_produto.erro: {e}')

async def deleta_produto(colecao, id_produto):
    try:
        ...
    except Exception as e:
        print(f'deleta_produto.error: {e}')
