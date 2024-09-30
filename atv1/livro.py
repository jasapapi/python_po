ano = 2024
class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao


            
    def exibirInformacoes(self):
       print (f"Informações do livro: \n {self.titulo}, {self.autor}, { self.anoPublicacao}.")
  
    def verificarIdadelivro(self):
        idade = ano - self.anoPublicacao
        if idade > 50:
            print("Esse livro é um clássico.")
        else:
            print("Esse livro ainda não é considerado um clássico.")

