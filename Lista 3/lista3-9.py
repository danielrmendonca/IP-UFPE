qtd_pokemons = input().split(" ") 
qtd_ash = int(qtd_pokemons[0])
qtd_gary = int(qtd_pokemons[1])

pokemons_ash = []
for a in range(qtd_ash):
    pokemon_ash = input().split(", ")
    pokemon_ash[2] = int(pokemon_ash[2])
    pokemon_ash[3] = int(pokemon_ash[3])
    pokemons_ash.append(pokemon_ash)

pokemons_gary = []
for g in range(qtd_gary):
    pokemon_gary = input().split(", ")
    pokemon_gary[2] = int(pokemon_gary[2])
    pokemon_gary[3] = int(pokemon_gary[3])
    pokemons_gary.append(pokemon_gary)

print("QUE COMECEM AS BATALHAS")
batalhas = 0
historico = []
vitorias_ash = 0
vitorias_gary = 0

while len(pokemons_ash) != 0 and len(pokemons_gary) != 0:
    entrada = input()
    if entrada == "FIM DAS BATALHAS":
        break

    decisao_ash = entrada
    numeros_ip = input().split(" ")
    numero_ash = int(numeros_ip[0])
    numero_gary = int(numeros_ip[1])

    escolha_pokemon_ash = input()
    escolha_pokemon_gary = input()
    nome_pokemon_ash = escolha_pokemon_ash.split(" eu escolho você!")[0]
    nome_pokemon_gary = escolha_pokemon_gary.split(" chegou a sua vez!")[0]

    numero = numero_ash + numero_gary
    if (numero % 2 == 0 and decisao_ash == "par") or (numero % 2 != 0 and decisao_ash == "ímpar"):
        turno_ash = True
    else:
        turno_ash = False

    hp_ash = 0
    nivel_ash = 0
    for s in range(len(pokemons_ash)):
        if pokemons_ash[s][0] == nome_pokemon_ash:
            hp_ash = pokemons_ash[s][2]
            nivel_ash = pokemons_ash[s][3]
            break

    hp_gary = 0
    nivel_gary = 0
    for a in range(len(pokemons_gary)):
        if pokemons_gary[a][0] == nome_pokemon_gary:
            hp_gary = pokemons_gary[a][2]
            nivel_gary = pokemons_gary[a][3]
            break

    while hp_ash > 0 and hp_gary > 0:
        if turno_ash:
            dano = nivel_ash * 2
            hp_gary -= dano
            turno_ash = False
        else:
            dano = nivel_gary * 2
            hp_ash -= dano
            turno_ash = True

    if hp_ash > hp_gary:
        print(f"{nome_pokemon_gary} desmaiou e {nome_pokemon_ash} venceu esta luta")
        historico.append(f"{nome_pokemon_ash.upper()} vs {nome_pokemon_gary.lower()}")
        vitorias_ash += 1
        for i in range(len(pokemons_gary)):
            if pokemons_gary[i][0] == nome_pokemon_gary:
                pokemons_gary.pop(i)
                break
    elif hp_ash < hp_gary:
        print(f"{nome_pokemon_ash} desmaiou e {nome_pokemon_gary} venceu esta luta")
        historico.append(f"{nome_pokemon_ash.lower()} vs {nome_pokemon_gary.upper()}")
        vitorias_gary += 1
        for i in range(len(pokemons_ash)):
            if pokemons_ash[i][0] == nome_pokemon_ash:
                pokemons_ash.pop(i)
                break

    batalhas += 1

print("=============== ===============")
if batalhas > 0:
    for i in range(batalhas):
        print(f"{i+1}° Batalha: {historico[i]}")
    if vitorias_ash > vitorias_gary:
        print("Ash é o grande vencedor!")
    elif vitorias_ash < vitorias_gary:
        print("Gary é o grande vencedor!")
    else:
        print("Depois de todas as batalhas, ainda terminou em empate!")
else:
    if len(pokemons_ash) == 0 and len(pokemons_gary) == 0:
        print("Nenhuma batalha foi concluída.")
    else:
        if len(pokemons_ash) == 0:
            print("Ash deixou seus pokemons descansando!")
            print("Gary é o grande vencedor!")
        else:
            print("Gary deixou seus pokemons descansando!")
            print("Ash é o grande vencedor!")
