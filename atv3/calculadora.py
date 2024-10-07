class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def construtor(self):
        print(f"\nOs números utilizados serão {self.num1} e {self.num2}.")

    def somar(self):
        print(f"Soma: {self.num1+self.num2}")

    def subtrair(self):
        print(f"Subtração: {self.num1-self.num2}")

    def multiplicar(self):
        print(f"Multiplicação: {self.num1*self.num2}")

    def dividir(self):
        if self.num2 != 0:
            print(f"Divisão: {self.num1/self.num2}")
        else:
            print(f"O segundo valor tem que ser diferente de 0.")

    def potencia(self):
        print(f"A pontecialização entre os valores é {self.num1**self.num2}")

    def verificarParImpar(self, valor):
        if valor % 2 == 0:
            print(f"{valor} é par.")
        else:
            print(f"{valor} é impar.")
