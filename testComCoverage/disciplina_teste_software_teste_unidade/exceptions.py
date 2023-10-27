class TipoIncorretoException(BaseException):

    def __init__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class AnoInvalidoException(BaseException):

    def __init__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class QuantidadeInvalidaException(BaseException):

    def __init__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem