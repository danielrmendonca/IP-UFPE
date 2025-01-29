alunos = input()
fila = alunos.split("-")
nomes = fila
trocas = [0] * len(fila)

while True:
    entrada = input()
    
    if entrada == "Acabou!":
        break
    else:
            
        alunos_troca = entrada.split("-")
        nome_1 = alunos_troca[0]
        nome_2 = alunos_troca[1]
        
        if nome_1 in fila and nome_2 in fila:

            indice_1 = fila.index(nome_1)
            indice_2 = fila.index(nome_2)

            trocas[indice_1] += 1
            trocas[indice_2] += 1

            fila[indice_1], fila[indice_2] = fila[indice_2], fila[indice_1]

        else:
            print("Essa dupla não esta na lista!")

print("Fila do almoço: ")
contador = 0
for i in fila:
    if contador == 1:
        tp = "teleporte!"
    else:
        tp = "teleportes!"

    aluno = fila.index(i)

    print(f"{fila[aluno]}: {trocas[contador]} {tp}")
    contador += 1
