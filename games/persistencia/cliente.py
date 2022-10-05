async def cria_cliente(colecao, cliente):
    try:
        ...

    except Exception as e:
        print(f'cria_cliente.erro: {e}')

async def pesquisa_cliente(colecao, id_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_cliente.erro: {e}')

async def pesquisa_cliente_pelo_email(colecao, email_cliente):
    try:
        ...
    except Exception as e:
        print(f'pesquisa_cliente_pelo_email.erro: {e}')

async def pesqusa_clientes(colecao, skip, limit):
    try:
        ## Realiza busca paginada de todos os clientes cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        clientes = await cursor.to_list(length=int(limit))
        return clientes

    except Exception as e:
        print(f'pesqusa_clientes.erro: {e}')

async def atualiza_cliente(colecao, id_cliente, dados_cliente):
    try:
        ...

    except Exception as e:
        print(f'atualiza_cliente.erro: {e}')

async def deleta_cliente(colecao, id_cliente):
    try:
        ...

    except Exception as e:
        print(f'deleta_cliente.erro: {e}')
