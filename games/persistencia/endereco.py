async def cria_endereco(colecao, endereco):
    try:
        ...

    except Exception as e:
        print(f'cria_endereco.erro: {e}')

async def pesquisa_endereco(colecao, id_endereco):
    try:
        ...

    except Exception as e:
        print(f'pesquisa_endereco.erro: {e}')

async def pesquisa_enderecos_pelo_email_cliente(colecao, email_cliente):
    try:
        ...

    except Exception as e:
        print(f'pesquisa_enderecos_pelo_email_cliente.erro: {e}')

async def pesqusa_enderecos(colecao, skip, limit):
    try:
        ## Realiza busca paginada de todos os endereços cadastros no banco
        cursor = colecao.find().skip(int(skip)).limit(int(limit))
        enderecos = await cursor.to_list(length=int(limit))
        return enderecos

    except Exception as e:
        print(f'pesqusa_enderecos.erro: {e}')

async def atualiza_endereco(colecao, id_endereco, dados_endereco):
    try:
        ...

    except Exception as e:
        print(f'atualiza_endereco.erro: {e}')

async def deleta_endereco(colecao, id_endereco):
    try:
        ...

    except Exception as e:
        print(f'deleta_endereco.erro: {e}')
