nome_jogador1 = str(input())
pontuacao_jogador1 = int(input())
nome_jogador2 = str(input())
pontuacao_jogador2 = int(input())
nome_jogador3 = str(input())
pontuacao_jogador3 = int(input())

if nome_jogador1 == 'Rodri' or nome_jogador2 == 'Rodri' or nome_jogador3 == 'Rodri':
   melhor_jogador = 'Rodri'
   if nome_jogador1 == melhor_jogador:
       melhor_pontuacao = pontuacao_jogador1
   elif nome_jogador2 == melhor_jogador:
       melhor_pontuacao = pontuacao_jogador2
   else: melhor_pontuacao = pontuacao_jogador3
   print(f'O melhor jogador do mundo é {melhor_jogador}, com {melhor_pontuacao} ponto(s).')
   print('Os europeus, como sempre, roubaram o nosso ouro!')

elif pontuacao_jogador1 > pontuacao_jogador2 and pontuacao_jogador1 > pontuacao_jogador3:
    print(f'O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s).')
    if nome_jogador1 == 'Vini Jr.':
        print('Os brasileiros amaram o resultado! BAILA VINI!')
    else: print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')

elif pontuacao_jogador2 > pontuacao_jogador1 and pontuacao_jogador2 > pontuacao_jogador3:
     print(f'O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s).')
     if nome_jogador2 == 'Vini Jr.':
        print('Os brasileiros amaram o resultado! BAILA VINI!')
     else: print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')

elif pontuacao_jogador3 > pontuacao_jogador1 and pontuacao_jogador3 > pontuacao_jogador2:
     print(f'O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s).')
     if nome_jogador3 == 'Vini Jr.':
        print('Os brasileiros amaram o resultado! BAILA VINI!')
     else: print('Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!')