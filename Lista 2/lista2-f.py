numero_renas = int(input())
numero_voltas = int(input())

if numero_renas < 3:
    print("Meu senhor, com essa quantidade de rena vai ter que entregar os presentes a pé, viu?!")
elif numero_renas == 3:
    for i in range(numero_renas):
        nome = input()
        if i == 0:
            nome1 = nome+", "
        elif i == 1:
            nome2 = nome+" e "
        elif i == 2:
            nome3 = nome+"."
    print("Como só temos 3 renas aptas pro serviço esse ano, não adianta muito querer ficar escolhendo")
    print("As três únicas renas capazes de participar esse ano são:")
    print(nome1 + nome2 + nome3)
    print("Não haverá teste de desempenho entre elas!")

else:
    top1_pontos = -1
    top2_pontos = -1
    top3_pontos = -1
    top1_rena = ""
    top2_rena = ""
    top3_rena = ""

    for i in range (numero_renas):
        nome = input()
        pontos_iniciais = 0

        for vogal in nome:
            if vogal == "A" or vogal == "a":
                pontos_iniciais += 8
            elif vogal == "E" or vogal == "e":
                pontos_iniciais += 5
            elif vogal == "I" or vogal == "i":
                pontos_iniciais += 4
            elif vogal == "O" or vogal == "o":
                pontos_iniciais += 3
            elif vogal == "U" or vogal == "u":
                pontos_iniciais += 2
        
        pontos = pontos_iniciais

        rodada = 1
        while rodada <= numero_voltas:
            if pontos % rodada == 0:
                pontos += 2
            elif (pontos % rodada) / 2 == 0:
                pontos += 1
            
            rodada += 1


        if pontos > top1_pontos:
            top3_rena = top2_rena
            top3_pontos = top2_pontos

            top2_rena = top1_rena
            top2_pontos = top1_pontos
            
            top1_rena = nome
            top1_pontos = pontos
  
        elif pontos > top2_pontos:
            top3_rena = top2_rena
            top3_pontos = top2_pontos

            top2_rena = nome
            top2_pontos = pontos

        elif pontos > top3_pontos:
            top3_rena = nome
            top3_pontos = pontos

    print("As três renas mais atléticas pra temporada de Natal são:")
    print(top1_rena + ", " + top2_rena + " e " + top3_rena + ".")