suspeito1 = str(input())
distancia1 = int(input())
suspeito2 = str(input())
distancia2 = int(input())

culpado = 'inocentes'

distancia_entre = ((distancia1**2) +(distancia2**2))**0.5
if (distancia_entre % 2) == 0:
    culpado = 'cúmplices'
else:
    categoria1 = str(input())
    categoria2 = str(input())
    
    if categoria1 == categoria2:

        if categoria1 == 'Fã':
            if (distancia1 % 2) == 0 and (distancia1 % 3) == 0 and (distancia2 % 2) == 0 and (distancia2 % 3) == 0:
                culpado = 'cúmplices'
            else:
                if (distancia1 % 2) == 0:
                    culpado = suspeito2
                elif (distancia2 % 3) == 0:
                    culpado = suspeito1

        elif categoria1 == 'Jogador':
            if (distancia1 % 2) == 0 and (distancia1 % 5) == 0 and (distancia2 % 2) == 0 and (distancia2 % 5) == 0:
                culpado = 'cúmplices'
            else:
                if (distancia1 % 2) == 0:
                    culpado = suspeito2
                elif (distancia2 % 5) == 0:
                    culpado = suspeito1

        else:
            if (distancia1 % 3) == 0 and (distancia1 % 5) == 0 and (distancia2 % 3) == 0 and (distancia2 % 5) == 0:
                culpado = 'cúmplices'
            else:
                if (distancia1 % 3) == 0:
                    culpado = suspeito2
                elif (distancia2 % 5) == 0:
                    culpado = suspeito1

    else:
        if distancia1 < distancia2:
            culpado = suspeito1
        elif distancia2 < distancia1:
            culpado = suspeito2
        else: culpado = 'inocentes'


if culpado == suspeito1:
    print(f'{suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!')
elif culpado == suspeito2:
    print(f'{suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!')
elif culpado == 'inocentes':
    print(f'{suspeito1} e {suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!')
elif culpado == 'cúmplices':
    print(f'{suspeito1} e {suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!')