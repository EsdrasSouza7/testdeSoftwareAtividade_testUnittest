import pytest

from livro import Livro, Exemplar
from exceptions import TipoIncorretoException, AnoInvalidoException,QuantidadeInvalidaException

def test_criar_novo_livro():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

    assert novo_livro.titulo == "The Art of Software Testing"
    assert novo_livro.autores == ["John Glenford Myers", "Corey Sandler", "Tom Badget"]
    assert novo_livro.ano_publicacao == 1976

def test_criar_Exemplar_com_tipo_incorreto():
    with pytest.raises(TipoIncorretoException):
        exemplar = Exemplar(1, 10, 1, 2023, "Editora")
        exemplar.livro = 2
