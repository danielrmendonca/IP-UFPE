animes_favoritos = [
    'Fullmetal Alchemist: Brotherhood',
    'Attack On Titan',
    'Death Note',
    'Naruto',
    'One Piece',
    'Demon Slayer',
    'Dragon Ball Z',
    'Jujutsu Kaisen',
    'Pokemon',
    'Bleach'
]

pontuacao = [0] * len(animes_favoritos)

numero_amigos = int(input())
print(f"{numero_amigos} amigos participaram da votação!")

for i in range(1, numero_amigos+1):
    nome = input()
    print(f"{nome} é a {i}ª pessoa à votar!")
    voto_top3 = []
    ordem = 1

    while len(voto_top3) < 3:
        voto = input().title()

        if voto in animes_favoritos:

            if voto in voto_top3:
                print(f"{nome}, você já votou neste anime! Escolha um outro anime para ocupar a sua {ordem}º posição!")
            else:
                voto_top3.append(voto)
                print(f"{nome} colocou {voto} em {ordem}º lugar do seu ranking!")
                indice = animes_favoritos.index(voto)
                if ordem == 1:
                    pontuacao[indice] += 3
                elif ordem == 2:
                    pontuacao[indice] += 2
                elif ordem == 3:
                    pontuacao[indice] += 1
                ordem += 1

        else:
                print(f"O anime {voto} não está presente na votação!")

pont_top1 = max(pontuacao)
indice1 = pontuacao.index(pont_top1)
nome_top1 = animes_favoritos[indice1]

print(f"Com {pont_top1} pontos, {nome_top1} foi votado como o melhor anime!")
if nome_top1 == "Pokemon":
    print("César - Pokémon é o melhor anime da história!!!")
print("Eita mandaram dúvida no discord, vou lá responder!")
