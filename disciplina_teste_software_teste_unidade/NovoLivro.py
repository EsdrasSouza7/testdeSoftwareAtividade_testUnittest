import unittest

from livro import Livro

class NovoLivro(unittest.TestCase):
    def test_novo_livro(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

        self.assertEqual("The Art of Software Testing", novo_livro.titulo )  # add assertion here
        self.assertEqual(["John Glenford Myers", "Corey Sandler", "Tom Badget"], novo_livro.autores)
        self.assertEqual(1976, novo_livro.ano_publicacao)


# if __name__ == '__main__':
    # unittest.main()
