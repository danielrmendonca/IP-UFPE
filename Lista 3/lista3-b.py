alunos = input()
fila = alunos.split("-") #lista com os alunos na fila
nomes = fila.copy() #fila sem alterações
trocas = [0] * len(nomes)

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
            fila[indice_1], fila[indice_2] = fila[indice_2], fila[indice_1]

            indice_para_troca_1 = nomes.index(nome_1)
            indice_para_troca_2 = nomes.index(nome_2)
            trocas[indice_para_troca_1] += 1
            trocas[indice_para_troca_2] += 1

        else:
            print("Essa dupla não esta na lista!")
print("Fila do almoço:")

for i in fila:
    indice = nomes.index(i)

    if trocas[indice] == 1:
        tp = "teleporte!"
    else:
        tp = "teleportes!"

    print(f"{nomes[indice]}: {trocas[indice]} {tp}")
