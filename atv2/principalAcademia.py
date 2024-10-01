from academia import Aluno

a1 = Aluno ("Anna","16", 62.0, 1.65 )
a1.exibirDados()
a1.calcularImc()

nomeAluno = (input("Digite seu nome: "))
idadeAluno = int (input("Digite sua idade: "))
pesoAluno = float (input("Digite seu peso: "))
alturaAluno = float (input("Digite sua altura: "))

a2 = Aluno(nomeAluno, idadeAluno, pesoAluno, alturaAluno)
a2.exibirDados()
a2.calcularImc()


