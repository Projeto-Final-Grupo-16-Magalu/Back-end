class RegraExcecao(Exception):
    def __init__(self, mensagem: str) -> None:
        super(RegraExcecao, self).__init__(mensagem)
        self.mensagem = mensagem


class NaoEncontradoExcecao(RegraExcecao):
    def __init__(self, mensagem: str) -> None:
        super(NaoEncontradoExcecao, self).__init__(mensagem)


class OutroRegistroExcecao(RegraExcecao):
    def __init__(self, mensagem: str) -> None:
        super(OutroRegistroExcecao, self).__init__(mensagem)
