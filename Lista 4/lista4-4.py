def descriptografar(codigo, deslocamento):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto = list(alfabeto)
    codigo = list(codigo)
    codigo_resolvido = ""
    for i in codigo:
        indice = alfabeto.index(i)
        indice_cesar = indice - deslocamento
        if indice_cesar < 0:
            indice_cesar += 26
        elif indice_cesar > 26:
            indice_cesar -= 26
        codigo_resolvido += alfabeto[indice_cesar]
    return codigo_resolvido

def calcular_dano(precisao, poder_explosao, resistencia, fator):
    dano = precisao * (poder_explosao / resistencia) * fator
    return dano

def ordenar_ataques (lista): #não vou usar sorted porque parece que não deve ser usado, mas a questão não especificou
    for i in range (len(lista)):
        maior = i
        for n in range (i+1, (len(lista))):
            if lista[n][1] > lista[maior][1]:
                maior = n
        lista[i], lista[maior] = lista[maior], lista[i]
    return lista

    
n_ataques = int(input())
if n_ataques == 0:
    print("Piltover em paz... por enquanto.")
else:
    ataques = []
    for ataque in range (n_ataques):
        entrada = input().split(", ")

        nome_alvo = entrada[0]
        precisao = int(entrada[1])
        resistencia = int(entrada[2])
        poder_explosao = int(entrada[3])
        codigo = entrada[4]
        deslocamento = int(entrada[5])

        fator_multiplicador = descriptografar(codigo, deslocamento)
        if ataque == 0:
            print(f"Decifrando: {fator_multiplicador}")
        else: print(f"\nDecifrando: {fator_multiplicador}")
        if fator_multiplicador == "ALTO":
            fator = 2
        elif fator_multiplicador == "MEDIO":
            fator = 1.5
        else:
            fator = 1

        dano = round(calcular_dano(precisao, poder_explosao, resistencia, fator))
        print(f"{nome_alvo}: {dano} de dano calculado.")
        if dano >= 100:
            print(f"{nome_alvo} será destruído!")
        else:
            print(f"{nome_alvo} resistirá ao ataque.")
        ataques.append([nome_alvo, dano])
    prioridade_ataques = ordenar_ataques(ataques)
    print("\nPrioridade de ataques:")
    for i in prioridade_ataques:
        print(f"{i[0]} - {i[1]} de dano")