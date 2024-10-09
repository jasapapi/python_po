dano = 24
class Personagem:
    def __init__(self, nome, vida, rank):
        self._nome = nome
        self._vida = vida
        self._rank= rank

    def receberDano(self, dano):
        self._vida -= dano
        print(f"{self._vida} - {dano}")

    def verificarVida(self):
        if self._vida <= 0:
            print(f"{self._nome} morreu")
        else:
            print(f"{self._nome} está vivo com {self._vida} de pontos de vida.")

    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Rank: {self._rank}")

class Heroi (Personagem):
    def __init__(self, nome, vida, rank, identidadeSecreta, energia):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidadeSecreta 
        self._energia = energia

    def executarHabilidade (self, tipoHabilidade):
        self._energia = self._energia - 15
        print (f"A habilidade {tipoHabilidade} foi ativida. Você perdeu 15 pontos da sua energia.")

    def recarregarEnergia(self):
        self._energia = self._energia + 8

    def chamarAliado (self, nomeAliado):
        print (f"O aliado {nomeAliado} foi chamado pelo herói para ajudar na luta. {nomeAliado} possui a Tempestade de Vento, ela invoca um poderoso tornado que causa dano aos inimigos e os arremessa para longe.")
        
class Vilao (Personagem):
    def __init__(self, nome,  vida, rank, malicia):
        super().__init__(nome, vida, rank)
        self._malicia = malicia

    def desferirGolpe (self, tipoGolpe):
        self._malicia = self._malicia - 20
        print (f"O golpe {tipoGolpe} foi usado e foi potencializado pela malícia do vilão. Foram usados 20 pontos de malícia.")

    def planejarArmadilha (self, tipoArmadilha):
        print (f"O vilão está planejando uma armadilha, a {tipoArmadilha}.")

    def fugir (self, tipoFulga):
        print (f"O vilão conseguiu escapar. Ele usou a {tipoFulga}. O vilão cria uma ilusão de si mesmo, enganando os inimigos enquanto ele foge para um local seguro, sem ser visto.")