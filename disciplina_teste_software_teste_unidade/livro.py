from exceptions import TipoIncorretoException, AnoInvalidoException, QuantidadeInvalidaException
class Livro():

    def __init__(self, titulo:str, autores:list, ano_publicacao:int):
        self._titulo = titulo
        self._autores = autores
        self._ano_publicacao = ano_publicacao

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autores(self):
        return self._autores

    @autores.setter
    def autores(self, autores):
        self._autores = autores

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, ano_publicacao):
        self._ano_publicacao = ano_publicacao

class Exemplar():

    def __init__(self, livro:Livro, quantidade:int, edicao:int, ano:int, editora:str):
        self._livro = livro
        self._quantidade = quantidade
        self._edicao = edicao
        self._ano = ano
        self._editora = editora

    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, livro):
        if isinstance(livro, Livro):
            self._livro = Livro
        else:
            raise TipoIncorretoException("Objeto não é do tipo Livro!")

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade >= 0:
            self._quantidade = quantidade
        else:
            raise QuantidadeInvalidaException("A quantidade deve ser maior ou igual a 0.")

    def adicionar_exemplares(self, quantidade):
        if quantidade > 0:
            self._quantidade += quantidade
        else:
            raise QuantidadeInvalidaException("A quantidade a ser adicionada deve ser maior do que 0.")

    def remover_exemplares(self, quantidade):
        if quantidade > 0:
            self._quantidade -= quantidade
        else:
            raise QuantidadeInvalidaException("A quantidade de livros a ser removida deve ser "
                                              "maior do que 0.")

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, edicao):
        self._edicao = edicao

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        if ano >= self._livro.ano_publicacao:
            self._ano = ano
        else:
            raise AnoInvalidoException("O ano do exemplar deve ser maior "
                                       "ou igual ao ano de publicação do livro!")

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, editora):
        self._editora = editora


