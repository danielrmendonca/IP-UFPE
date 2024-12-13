plateia_1 = input()
plateia_2 = input()
vencedor = input()

if vencedor == 'Palé' or (plateia_1 == 'Gavião Bonito' and plateia_2 == 'Ronaldinho Paulista') or (plateia_2 ==  'Gavião Bonito' and plateia_1 == 'Ronaldinho Paulista'):
    print('Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!')
elif vencedor == 'Mãodona':
    if (plateia_1 == 'Gavião Bonito' and plateia_2 != 'Ronaldinho Paulista') or (plateia_1 != 'Ronaldinho Paulista' and plateia_2 == 'Gavião Bonito'):
        print('Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…')
    elif (plateia_1 != 'Gavião Bonito' and plateia_2 == 'Ronaldinho Paulista') or (plateia_2 != 'Gavião Bonito' and plateia_1 == 'Ronaldinho Paulista'):
        print('Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…')
    else:
        print('PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto.')
else:
    print('Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.')