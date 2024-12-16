rodadas = int(input())
rodada = 0
meias_duendes = 0
meias_elfos = 0
desafio_dificil = 0
dd_duendes = 0
dd_elfos = 0
meias = 0
print("O Torneio de Natal começa agora! Que vençam os melhores!")

for i in range (rodadas):
    meias_rodada = meias
    meias = 0
    rodada += 1
    print(f"RODADA {rodada}")
    equipe = str(input())
    desafio = str(input())
    dificuldade = str(input())

    if desafio == "Prepararam as roupas do Papai Noel." or desafio == "Alimentaram as renas.":
        meias_rodada += 10
    elif desafio == "Arrumaram os estoques de doces." or desafio == "Guardaram os presentes no trenó.":
        meias_rodada += 20
    elif desafio == "Ajudaram a carregar os presentes." or desafio == "Embrulharam os presentes." or desafio == "Decoraram a árvore de Natal.":
        meias_rodada += 30
    elif desafio == "Planejaram a rota do Papai Noel.":
        meias_rodada += 50
    elif desafio == "Testaram os brinquedos.":
        quantidade_brinquedos = int(input())
        meias_rodada += quantidade_brinquedos * 2
    
    if dificuldade == "Médio":
        meias_rodada += meias_rodada * 0.2
    elif dificuldade == "Difícil":
        meias_rodada += meias_rodada * 0.5
        desafio_dificil +=1
    
    evento_surpresa = str(input())

    if evento_surpresa == "Dia de Sorte":
        meias_rodada += 30
        print("É um Dia de Sorte! Vocês ganharam 30 meias bônus!")
    elif evento_surpresa == "Dia de Azar":
        meias_rodada -= 30
        print("É um Dia de Azar! Vocês perderam 30 meias!")
        if meias_rodada < 0:
            meias_rodada = 0
    elif evento_surpresa == "Grinch":
        print("O Grinch está sabotando o Torneio!")
        condicao = 0
        while condicao == 0:

            cor = str(input())
            if cor == "Amarelas":
                meias_rodada -= 5
            elif cor == "Verdes":
                meias_rodada -= 10
            elif cor == "Vermelhas":
                meias_rodada -= 20
            elif cor == (f"{equipe}, protejam as meias!"):
                condicao = 1

            if meias_rodada < 0:
                meias_rodada = 0

    if meias_rodada > 0:
        print(f"A equipe dos {equipe} ganhou {int(meias_rodada)} meias nesta rodada.")
    elif meias_rodada == 0:
        print(f"Infelizmente, a equipe dos {equipe} não ganhou meias nessa rodada.")

    if equipe == "Duendes":
        meias_duendes += meias_rodada
        dd_duendes += desafio_dificil
    else:
        meias_elfos += meias_rodada
        dd_elfos += desafio_dificil

    if meias_duendes > meias_elfos:
        equipe_vencedora = "Duendes"
        meias_vencedora = meias_duendes
    elif meias_elfos > meias_duendes:
        equipe_vencedora = "Elfos"
        meias_vencedora = meias_elfos
    else:
        if dd_duendes > dd_elfos:
            equipe_vencedora = "Duendes"
            meias_vencedora = meias_duendes
        elif dd_elfos > dd_duendes:
            equipe_vencedora = "Elfos"
            meias_vencedora = meias_elfos

print("TORNEIO ENCERRADO!")
print("Segurem seus gorros que o Noel já vai entregar o Prêmio da Estrela Natalina.")
print(f"Os {equipe_vencedora} venceram o Torneio de Natal com um total de {int(meias_vencedora)} meias e terão a honra de ajudar o Papai Noel na noite mais mágica do ano.")