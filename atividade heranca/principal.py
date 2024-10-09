from personagem import Personagem, Heroi, Vilao

person1 = Personagem ("Labi", 100, "Intemediário")
heroi1 = Heroi("Ryle", 100, "Intemediário","Destino", 50)
vilao1 = Vilao ("Lorde", 100, "Avançado", 70)

heroi1.detalhes()
heroi1.executarHabilidade("Lâmina Dourada")
heroi1.recarregarEnergia()
heroi1.chamarAliado ("Feiticeira do Vento")

vilao1.detalhes()
vilao1.desferirGolpe ("Manipulacão da Sombras")
vilao1.planejarArmadilha ("Rede Suspensa")
vilao1.fugir ("Ilusão de Corpo")

person1.detalhes()