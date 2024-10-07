class Celular:
    def __init__(self, numero, saldo, plano, valorMinuto=1.50):
        self.__numero = numero
        self.__saldo = saldo
        self.__plano = plano
        self.__valorMinuto = valorMinuto

def construtor(self):
    print(f"Número de telefone: {self.__numero} \nSaldo: {self.__saldo} \nPlano: {self.__plano} \n")

@property
def plano(self):
    return self.__plano

@plano.setter
def plano(self, novo_plano):
    self.__plano = novo_plano
    if novo_plano == "pré-pago":
        self.__saldo = self.__saldo + self.recarregar

def recarregar(self, valor):
    self.recarregar = valor

def fazerChamadas(self, duracao_minutos):
    self.fazerChamadas = duracao_minutos

def exibirDados(self):
    if self.novo_plano == "pré-pago":
        if self.__saldo < self.__valorMinuto * self.fazerChamdas:
            print("O saldo é insuficiente para cobrir o custo da chamada.\n")
            
            print(f"Dados atuais: \nNúmero de telefone: {self.__numero} \nPlano: {self.__plano} \nSaldo: {self.__saldo + self.recarregar} \nCusto da chamada: {self.__valorMinuto * self.fazerChamdas}")

        else: 
            print(f"Dados atuais: \nNúmero de telefone: {self.__numero} \nPlano: {self.__plano} \nSaldo atual: {(self.__saldo - (self.__valorMinuto * self.fazerChamadas)) + self.recarregar}") 

    if self.novo_plano == "pós-pago":
        print(f"Dados atuais: \nNúmero de telefone: {self.__numero} \nPlano: {self.__plano} \nSaldo atual: {self.__saldo }\n") 
        print(f"O valor à ser cobrado no final do mês: {self.__valorMinuto * self.fazerChamadas}")

