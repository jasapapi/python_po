from datetime import datetime
class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"Título: {self._titulo} \nAutor: {self._autor} \nAno de Publicção: {self._anoPublicacao} \nNúmero da Página: {self._numeroPagina}")

    def calcularIdadeItem(self):
        ano_atual = 2024
        idade = ano_atual - self._anoPublicacao

        if idade > 70:
            categoria = "muito antigo"

        elif 30 <= idade <= 70:
            categoria = "recente"
        
        else:
            categoria = "contemporâneo"
        print(f"{self._titulo} ({self._anoPublicacao}) - idade: {idade} anos \nClassificação: {categoria}")

class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            Tamanho = "longo"

        else:
            Tamanho = "curto"
        print(f"{self._titulo} - Páginas: {self._numeroPagina} \nClassificação: {Tamanho}")

class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao < 1998:
            edicao = "edição especial"
        else:
            edicao = "não é uma edição especial"
        print(f"{self._titulo}, ({self._anoPublicacao}): {edicao}")