def pontuacao(aprovacao, orcamento, categoria):
    pontuacao = 0
    if aprovacao == "APROVA":
        pontuacao += 5
    elif aprovacao == "TANTO FAZ":
        pontuacao += 2
    
    if orcamento > 1000000:
        pontuacao += 3
    elif orcamento >= 500000:
        pontuacao += 4
    else:
        pontuacao += 5
    
    if categoria == "Defesa":
        pontuacao += 5
    elif categoria == "Ciencia":
        pontuacao += 4
    elif categoria == "Lazer":
        pontuacao += 3

    return pontuacao

def ordenar_obras(obras):
    obras_ordenadas = dict(sorted(obras.items(), key=lambda ordem: (
        -(pontuacao(ordem[1]["aprovacao"], ordem[1]["orcamento"], ordem[1]["categoria"])), ordem[1]["orcamento"])))
    return obras_ordenadas

obras = {}
for entrada in range(3):
    nome_estabelecimento = input()
    aprovacao = input()
    orcamento = int(input())
    categoria = input()

    obras[nome_estabelecimento] = {"aprovacao": aprovacao, "orcamento": orcamento, "categoria": categoria}
    
obras_ordenadas = ordenar_obras(obras)
estabelecimentos_ordenados = list(obras_ordenadas.keys())

estabelecimento1, estabelecimento2, estabelecimento3 = estabelecimentos_ordenados[0], estabelecimentos_ordenados[1], estabelecimentos_ordenados[2]
orcamento1, orcamento2, orcamento3 = obras[estabelecimento1]["orcamento"], obras[estabelecimento2]["orcamento"], obras[estabelecimento3]["orcamento"]
categoria1, categoria2, categoria3 = obras[estabelecimento1]["categoria"], obras[estabelecimento2]["categoria"], obras[estabelecimento3]["categoria"]

print()
print(f"O primeiro estabelecimento construído deve ser {estabelecimento1}, com um orçamento de {orcamento1} e com a funcionalidade de {categoria1}.")
print(f"O segundo estabelecimento construído deve ser {estabelecimento2}, com um orçamento de {orcamento2} e com a funcionalidade de {categoria2}.")
print(f"O terceiro estabelecimento construído deve ser {estabelecimento3}, com um orçamento de {orcamento3} e com a funcionalidade de {categoria3}.")

for i in obras_ordenadas:
    if obras_ordenadas[i]["categoria"] == "Defesa":
        print("Oba, agora a cidade estará mais segura.")
    elif obras_ordenadas[i]["categoria"] == "Ciencia":
        print("Agora sim vou poder ter uma vida intelectual.")
    elif obras_ordenadas[i]["categoria"] == "Lazer":
        print("Vamooo, agora posso curtir meu final de semana descansando na bela cidade do Recife.")