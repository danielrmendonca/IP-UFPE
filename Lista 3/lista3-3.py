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

    if nome in aprimoradores:
            aprimoradores.remove(nome)
    if nome in emissores:
            emissores.remove(nome)
    if nome in transmutadores:
            transmutadores.remove(nome)
    if nome in manipuladores:
            manipuladores.remove(nome)
    if nome in conjuradores:
            conjuradores.remove(nome)
    if nome in especialistas:
            especialistas.remove(nome)

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
    print(f"Temos um total de {len(aprimoradores)} aprimoradores entre os monitores! Eles são: {', '.join(aprimoradores)}")

if len(emissores) > 0:
    print(f"Temos um total de {len(emissores)} emissores entre os monitores! Eles são: {', '.join(emissores)}")

if len(transmutadores) > 0:
    print(f"Temos um total de {len(transmutadores)} transmutadores entre os monitores! Eles são: {', '.join(transmutadores)}")

if len(manipuladores) > 0:
    print(f"Temos um total de {len(manipuladores)} manipuladores entre os monitores! Eles são: {', '.join(manipuladores)}")

if len(conjuradores) > 0:
    print(f"Temos um total de {len(conjuradores)} conjuradores entre os monitores! Eles são: {', '.join(conjuradores)}")

if len(especialistas) > 0:
    print(f"Temos um total de {len(especialistas)} especialistas entre os monitores! Eles são: {', '.join(especialistas)}")