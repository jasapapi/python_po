from livro import Livro


l1 = Livro("Diário de Anne Frank","Anne Frank",1947)
l1.exibirInformacoes()
l1.verificarIdadelivro()

tituloLivro = input("Título do livro: ")
autorLivro = input("Autor do livro: ")
anoLivro = int (input("Ano de publicação do livro: "))

l2 = Livro (tituloLivro,autorLivro, anoLivro)
l2.exibirInformacoes()
l2.verificarIdadelivro()
