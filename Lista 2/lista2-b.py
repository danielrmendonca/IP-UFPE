print("PLAYLIST DO PAPAI NOEL")
condição = 0
quantidade_musicas = 0
sabotagem = 0
playlist = 0

while condição == 0:
    musica = input()

    if musica == "FIM":
        if playlist > 0:
            print(f"Ufa! Conseguimos criar a playlist perfeita, tomara que o Papai Noel goste das {quantidade_musicas} músicas.")
        else:
            print("Infelizmente não conseguimos encontrar nenhuma música para a playlist do Papai Noel...")
        condição = 1

    elif musica.isnumeric() == True:
        sabotagem += 1
        if sabotagem == 3:
            print("NAAÃO! Já está na hora do Papai Noel sair e não conseguimos construir sua playlist perfeita.")
            condição = 1
        else:
            print("ABORTAR! OS VILÕES OBTIVERAM ACESSO, TEREMOS QUE RECOMEÇAR.")
            print("PLAYLIST DO PAPAI NOEL")
            playlist = 0
            quantidade_musicas = 0
    
    else:
        alfanumerico = True
        for i in musica:
            if not (i.isalpha() or i == " "):
                alfanumerico = False

        if len(musica.replace(" ", "")) >= 15:
            letras = True
        else: letras = False

        if alfanumerico == True and letras == True:
            print(f"{musica} foi adicionada à playlist!")
            playlist += 1
            quantidade_musicas += 1
            ultima_musica = musica
        elif playlist > 0:
            print(f"{musica} não pôde ser adicionada à playlist! A última música adicionada foi {ultima_musica}.")
        elif playlist == 0:
            print(f"{musica} não pôde ser adicionada e a playlist continua vazia. Papai Noel precisa da sua ajuda!")