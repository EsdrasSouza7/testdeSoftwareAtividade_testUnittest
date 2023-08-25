import unittest
from livro import Livro, Exemplar
from exceptions import TipoIncorretoException, QuantidadeInvalidaException, AnoInvalidoException

class TesteLivro(unittest.TestCase):

    def test_criar_novo_livro(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

        self.assertEqual(novo_livro.titulo, "The Art of Software Testing")  # add assertion here
        self.assertEqual(novo_livro.autores, ["John Glenford Myers", "Corey Sandler", "Tom Badget"])
        self.assertEqual(novo_livro.ano_publicacao, 1976)

    def test_criar_exemplar_com_livro_incorreto(self):
        exemplar = Exemplar(1, 10, 1, 2023, "Editora")
        with self.assertRaises(TipoIncorretoException):
            exemplar.livro = 2

    def test_exemplar_com_quantidade_zero(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        with self.assertRaises(QuantidadeInvalidaException):
            exemplar = Exemplar(novo_livro, 0, 1, 2022, "Editora")
    
    def test_criando_exemplar_corretamente(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        exemplar = Exemplar(novo_livro, 10, 1, 2022, "Editora")

        self.assertEqual(exemplar.livro, novo_livro)
        self.assertEqual(exemplar.quantidade, 10)
        self.assertEqual(exemplar.edicao, 1)
        self.assertEqual(exemplar.ano, 2022)
        self.assertEqual(exemplar.editora, "Editora")

    def test_remover_exemplares_corretamente(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        exemplar = Exemplar(novo_livro, 10, 1, 2022, "Editora")
        exemplar.remover_exemplares(5)
        self.assertEqual(exemplar.quantidade, 5)

    def test_remover_exemplares_incorretamente(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        exemplar = Exemplar(novo_livro, 10, 1, 2022, "Editora")
        with self.assertEqual(QuantidadeInvalidaException):
            exemplar.remover_exemplares(-5)
    
    def test_mudar_ano_do_exemplar_com_ano_incorreto(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        exemplar = Exemplar(novo_livro, 10, 1, 2022, "Editora")
        with self.assertEqual(AnoInvalidoException):
            exemplar.ano = 1970
    
    def test_criar_exemplar_com_ano_menor_que_o_livro(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers"], 2000)
        with self.assertEqual(AnoInvalidoException):
            exemplar = Exemplar(novo_livro, 10, 1, 1999, "Editora")
    
    
    
        
#pip install pipinv
#pipinv shell
# if __name__ == '__main__':
#     unittest.main()