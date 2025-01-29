qtd_monitores = int(input())

aprimoradores = []
emissores = []
transmutadores = []
manipuladores = []
conjuradores = []
especialistas = []

for i in range (qtd_monitores):
    nome = input()
    mudanca = input()

    if mudanca == "O volume da água foi alterado.":
        aprimoradores.append(nome)
    elif mudanca == "A cor da água foi alterada.":
        emissores.append(nome)
    elif mudanca == "O gosto da água foi alterado.":
        transmutadores.append(nome)
    elif mudanca == "A folha se moveu.":
        manipuladores.append(nome)
    elif mudanca == "Impurezas apareceram na água.":
        conjuradores.append(nome)
    else:
        especialistas.append(nome)

if len(aprimoradores) > 0:
    print(f"Temos um total de {len(aprimoradores)} aprimoradores entre os monitores! Eles são: {", ".join(aprimoradores)}")

