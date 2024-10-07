from calculadora import Calculadora


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

num3 = int(input("Digite o número que você quer saber se é par ou impar: "))

c1 = Calculadora (num1, num2)
c1.construtor()
c1.somar()
c1.multiplicar()
c1.dividir()
c1.potencia()
c1.verificarParImpar(num3)