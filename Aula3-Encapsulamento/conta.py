class Conta:
    def __init__(self, numero, titular, saldo, limite=200):#Estamos passando um valor padrão para p limite, tornando-o opcional, dessa froma o objeto ao ser criado pode ter limite informando ou não.
        #quando colocamos 2 underlines antes do atributo, indicamos que esse atributo está com a visibilidade "privado", o contrario significa que está publico
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def relatorio(self):
        print(f"Olá {self.__titular} seu saldo atual é {self.__saldo} e o seu limite atual é {self.__limite}.")

    def getLimite(self):
        return self.__limite
    
    def setLimite(self, valor):
        if valor < 0:
            print ("Informe um valor válido")
        else:
            self.__limite = valor

    def depositar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else: 
            self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            print("Saldo insuficiente ou valor negativo solicitado")
        else:
            self.__saldo -= valor

