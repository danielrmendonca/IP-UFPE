limite_animes = int(input())
quantidade_animes = int(input())
lista_animes = []

for i in range (quantidade_animes):
    entrada = input()
    nome_anime, quantidade_temporadas, quem_indicou = entrada.split(" - ")

    if len(lista_animes) == limite_animes:
        print(f"A lista de animes está cheia. O {nome_anime} não foi adicionado.")

    elif quem_indicou == "Walter":
        lista_animes.append(nome_anime)
        print(f"O {nome_anime} foi adicionado à lista de animes para assistir.")
    
    elif quem_indicou == "Internet" and int(quantidade_temporadas) <= 16:
        lista_animes.append(nome_anime)
        print(f"O {nome_anime} foi adicionado à lista de animes para assistir.")
    elif quem_indicou == "Internet" and int(quantidade_temporadas) > 16:
        print(f"O {nome_anime} é muito longo, fica pra próxima.")    

print(f"Lista final para assistir:{lista_animes}")