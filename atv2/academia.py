class Aluno:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def exibirDados(self):
        print(f"Ola {self.nome}, sua idade é {self.idade}, seu peso é {self.peso} e sua altura é {self.altura}.")

    def calcularImc(self):
        imc = self.peso/(self.altura*self.altura)
        print (f"Seu IMC é {imc:.2f}.")
