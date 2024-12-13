nome_jogador = str(input())
partidas = int(input())
gols = int(input())
assistencias = int(input())
desarmes = int(input())
liga = str(input())

if liga != 'Premier League' and liga != 'La Liga' and liga != 'Serie A' and liga != 'Brasileirão':
    print('A liga informada não é válida ou o jogador não pertence a nenhuma das ligas elegíveis para a premiação.')
elif (gols / partidas) < 0.3:
    print('O jogador está fora, não possui a média de gols necessária.')
elif (assistencias / partidas) < 0.15:
    print('Infelizmente não teve assistências o suficiente, portanto não concorre ao prêmio.')
elif (desarmes / partidas) < 1.25:
    print(f'{nome_jogador} não desarmou jogadores o suficiente, portanto está fora.')
elif partidas < 50:
    print('O atleta não jogou partidas o suficiente para concorrer à premiação.')
else:
    score = (gols * 2) + (assistencias) + (desarmes * 0.4)
    if liga == 'Premier League':
        score_final = score
    elif liga == 'La Liga':
        score_final = score * 0.95
    elif liga == 'Serie A':
        score_final = score * 0.9
    else: score_final = score * 0.8

    if score_final >= 80:
        print(f'Promissor! {nome_jogador} é um potencial ganhador da Bola de Ouro!')
    elif score_final >= 70:
        print(f'{nome_jogador} tem chances médias de ganhar o prêmio.')
    elif score_final < 70:
        print(f'{nome_jogador} dificilmente ganhará a premiação, apesar de ser apto.')

