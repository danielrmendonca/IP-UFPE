quantidade_membros = int(input())
condicao = 0
numero_filme = 0
filmes_fora = 0

print("MARATONA DE NATAL: PAVÊ, RABANADA E FILMES")
while condicao == 0:
    filme = str(input())
    if filme ==  "chega de filmes por hoje":
        condicao = 1
    else:
        
        nacionalidade_filme = str(input()).lower()

        if nacionalidade_filme == "brasil" or nacionalidade_filme == "br":
            nacional = True
            estrangeiro = False
        else:
            nacional = False
            estrangeiro = True

        if "natal" in filme.lower() or "papai noel" in filme.lower() or "magia" in filme.lower():
            filme_natalino = True
        else: filme_natalino = False

        if nacional == True and filme_natalino == True:
            numero_filme +=1 
            print(f"{numero_filme}º filme: {filme}")
            nota = 0
            for i in range (quantidade_membros):
                nota += int(input())
            media = nota / quantidade_membros
            print(f"Média de votos para '{filme}': {media:.1f}")
        
        if estrangeiro == True and filme_natalino == True:
            filmes_fora += 1 

print(f"{numero_filme} Filmes BR X {filmes_fora} Filmes FORA")

if numero_filme == 0:
    print("Infelizmente esse ano não será nem pa vê e nem pa comer, sua lista não possui um filme bom, ops… nacional")
elif numero_filme == 1:
    print("De toda sua lista, apenas UM filme de natal é nacional, melhore suas escolhas e tente novamente!")
else:
    print("A ceia está servida? Porque aqui estão os filmes brasileiros que vão dar o toque especial da sua maratona no Natal!")