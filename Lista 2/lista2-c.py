condicao = 0
tempo_total = 0
quantidade_presentes = 0
#v rena 80kmh
print("Boa noite, Papai Noel! Feliz Natal!")
while condicao == 0:
    informacao = input()
    if informacao == "Já está amanhecendo, preciso voltar ao Polo Norte! HO HO HO!":
        condicao = 1
    else:
        crianca = str(input())
        distancia = float(input())
        unidade = str(input())
        if unidade == "metros":
            distancia = distancia / 1000
        tempo = distancia / 80
        tempo_min = tempo * 60
        tempo_total += tempo
        quantidade_presentes += 1
        if tempo >= 1:
            print(f"Querido Papai Noel, você levará {int(tempo)} horas para chegar até a casa de {crianca}!")
        elif tempo < 1 and tempo_min >= 1:
            print(f"Querido Papai Noel, você levará {int(tempo_min)} minutos para chegar até a casa de {crianca}!")
        elif tempo_min < 1:
            print(f"Querido Papai Noel, você chegará em breve na casa de {crianca}!")

print(f"Querido Papai Noel, a noite de natal foi um sucesso! Você levou apenas {tempo_total:.2f} horas para entregar todos os {quantidade_presentes} presentes")

        