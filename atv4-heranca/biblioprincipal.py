from biblioteca import Livro, Revista

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, 80)
revista1 = Revista("Revista Veja", "Veja", 1997, 30)

print(livro1.detalhes())
print(livro1.calcularIdadeItem())
print(livro1.verificarTamanho())

print(revista1.detalhes())
print(revista1.calcularIdadeItem())
print(revista1.verificarEdicao())
