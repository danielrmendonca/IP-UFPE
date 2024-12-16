for i in range (1, 4):
    nome_musica = str(input())
    quantidade_streams = int(input())
    if i == 1:
        musica_1 = nome_musica
        streams_1 = quantidade_streams
    elif i == 2:
        musica_2 = nome_musica
        streams_2 = quantidade_streams
    elif i == 3:
        musica_3 = nome_musica
        streams_3 = quantidade_streams

if streams_1 > streams_2 and streams_1 > streams_3:
    top1_stream = streams_1
    top1_musica = musica_1
    if streams_2 > streams_3:
        top2_stream = streams_2
        top2_musica = musica_2
        top3_stream = streams_3
        top3_musica = musica_3
    else:
        top2_stream = streams_3
        top2_musica = musica_3
        top3_stream = streams_2
        top3_musica = musica_2
elif streams_2 > streams_1 and streams_2 > streams_3:
    top1_stream = streams_2
    top1_musica = musica_2
    if streams_1 > streams_3:
        top2_stream = streams_1
        top2_musica = musica_1
        top3_stream = streams_3
        top3_musica = musica_3
    else:
        top2_stream = streams_3
        top2_musica = musica_3
        top3_stream = streams_1
        top3_musica = musica_1
else:
    top1_stream = streams_3
    top1_musica = musica_3
    if streams_1 > streams_2:
        top2_stream = streams_1
        top2_musica = musica_1
        top3_stream = streams_2
        top3_musica = musica_2
    else:
        top2_stream = streams_2
        top2_musica = musica_2
        top3_stream = streams_1
        top3_musica = musica_1

print(f"1º: {top1_musica} teve {top1_stream} de streams e foi a música mais ouvida de Simone!")
print(f"2º: {top2_musica} teve {top2_stream} de streams e foi a segunda música mais ouvida de Simone!")
print(f"3º: {top3_musica} teve {top3_stream} de streams e completou o top 3 das músicas mais ouvidas da artista!")

if top1_stream > 10000000:
    print(f"Uau! {top1_musica} foi um hit certeiro da rainha do Natal!")
    if top2_stream > 10000000:
        print(f"Uau! {top2_musica} foi um hit certeiro da rainha do Natal!")
        if top3_stream >10000000:
            print(f"Uau! {top3_musica} foi um hit certeiro da rainha do Natal!")

if top1_stream < 1000000: #pra imprimir primeiro a melhor
    print(f"Bom… a música {top1_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
    print(f"Bom… a música {top2_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
    print(f"Bom… a música {top3_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
elif top2_stream < 1000000:
    print(f"Bom… a música {top2_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
    print(f"Bom… a música {top3_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")
elif top3_stream < 1000000:
    print(f"Bom… a música {top3_musica} não foi exatamente um sucesso nacional, mas foi o suficiente para entrar no topo da lista das mais ouvidas.")

if top1_stream - top2_stream > 5000000:
    print(f"{top1_musica} foi disparada a mais ouvida neste ano! Nenhuma outra música natalina chega aos pés dela!")
elif top1_stream - top2_stream < 1000000:
    print(f"{top1_musica} foi a mais ouvida, mas não podemos esquecer da música {top2_musica}! Fez bonito nesse feriado!")