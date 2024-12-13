jogador_1 = input()
pontuação_1 = int(input())

jogador_2 = input()
pontuação_2 = int(input())

jogador_3 = input()
pontuação_3 = int(input())

if jogador_1 == 'Lucas Lima' or jogador_2 == 'Lucas Lima' or jogador_3 == 'Lucas Lima':
    print('Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!') #Roubado
elif pontuação_1 > pontuação_2 and pontuação_1 > pontuação_3:
    print(f'{jogador_1} é eleito o bola de ouro!')
elif pontuação_2 > pontuação_1 and pontuação_2 > pontuação_3:
    print(f'{jogador_2} é eleito o bola de ouro!')
else: #Não haverá casos de emapte
    print(f'{jogador_3} é eleito o bola de ouro!')