from typing import List, Optional
from uuid import uuid4
from games.modelos import produto
from games.modelos.produto import Produto


async def cria_produto(produto: Produto):
    await validar_produto(produto)

    novo_produto = produto.dict()
    # Gerando novo código com uuidv4
    novo_produto[produto.CampoProduto.CODIGO] = str(uuid4())

    # Salvando no banco de dados
    await produto.cria_produto(novo_produto)

    # Retornando o registro da música completo
    produto_geral = Produto(**novo_produto)

    return produto_geral




async def pesquisa_produto_pelo_codigo(
    codigo: str, lanca_excecao_se_nao_encontrado: bool = False
) -> Optional[dict]:
    # Pesquisando pelo código no banco
    produto = await produto.pesquisa_produto_pelo_codigo(codigo)
    # Não encontrei, devo lançar exceção?
    if not produto and lanca_excecao_se_nao_encontrado:
        raise NaoEncontradoExcecao("Produto não encontrado")
    # Retornando o registro do banco.
    return produto


async def pesquisa_produtos() -> List[dict]:
    todos_produtos = await produto.pesquisa_produtos()
    return todos_produtos


async def validar_produto(produto: Produto, codigo_base: Optional[str] = None):
    produto_novo = codigo_base is None

    outro_produto = await produto.pesquisar_pelo_nome(produto.nome)
    if (outro_produto is not None) and (
        produto_novo or
        (codigo_base != outro_produto["CAMPO_CODIGO"])
    ):
        raise OutroRegistroExcecao("Há outra produto com este nome")





async def remover_por_codigo(codigo: str):
  
    removeu = await produto.remover_uma_produto_pelo_codigo(codigo)

    if not removeu:
        raise NaoEncontradoExcecao("Produto não encontrado")


async def atualiza_produto(codigo: str, produto: Produto):
    # Pesquisando produto para atualizar
    # Se não existe, lançamos a exceção.
    await atualiza_produto(codigo, True)

    # Se foi informado o código, vamos ver se não são diferentes
    if produto.codigo is not None and produto.codigo != codigo:
        # Sim na linha de abaixo não esquecemos dos parêntesis.
        # Por quê?
        raise CodigosDiferentesExcecao

    # Validando, com código; para identificar que é uma atualização
    validar_produto(produto, codigo)

    produto_para_banco = produto.dict()
    # Pequeno ajuste, se o código não existe, devemos retirá-lo
    if produto.codigo is None:
        produto_para_banco.pop("CAMPO_CODIGO", None)

    # Atualizando no banco de dado
    await produto.atualizar_uma_produto_pelo_codigo(
        codigo, produto_para_banco
    )




"""
Exceções das regras.
"""


class RegraExcecao(Exception):
    # Exceção geral das regras
    def __init__(self, mensagem: str) -> None:
        super(RegraExcecao, self).__init__(mensagem)
        self.mensagem = mensagem


class NaoEncontradoExcecao(RegraExcecao):
    # Exceção geral para um registro não encontrado.
    def __init__(self, mensagem: str) -> None:
        super(NaoEncontradoExcecao, self).__init__(mensagem)


class OutroRegistroExcecao(RegraExcecao):
    # Exceção de que há outro registro coincidindo...
    def __init__(self, mensagem: str) -> None:
        super(OutroRegistroExcecao, self).__init__(mensagem)

# 
class CodigosDiferentesExcecao(OutroRegistroExcecao):
    def __init__(self) -> None:
        super().__init__("Código diferentes")  