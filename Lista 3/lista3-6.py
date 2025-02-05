num_feiticeiros = int(input())
feiticeiros = []

for i in range (num_feiticeiros):
    nome = input()
    nivel = int(input())
    feiticeiros.append([nome, nivel])

num_rodada = 1
vencedores =[]
while len(feiticeiros) > 1:
    vencedores = []
    print(f"\n--- Rodada {num_rodada} ---")
    duelos = 0

    if len(feiticeiros) % 2 == 1:
        ultimo = feiticeiros.pop()
        impar = True
    else: impar = False

    while duelos < len(feiticeiros):
        print(f"Confronto: {feiticeiros[duelos][0]} vs {feiticeiros[duelos+1][0]}")

        if feiticeiros[duelos][1] >= feiticeiros[duelos+1][1]:
            vencedores.append(feiticeiros[duelos])
            print(f"{feiticeiros[duelos][0]} vence!")
        else:
            vencedores.append(feiticeiros[duelos+1])
            print(f"{feiticeiros[duelos+1][0]} vence!")
        duelos += 2

    if impar:
        print(f"{ultimo[0]} avança automaticamente!")
        vencedores.append(ultimo)
    feiticeiros = vencedores.copy()
    num_rodada +=1

nome_campeao = feiticeiros[0][0]
nivel_campeao = feiticeiros [0][1]

print(f"\nO campeão do torneio é {nome_campeao} com nível de energia amaldiçoada {nivel_campeao}!")

if nome_campeao == "Itadori":
    if nivel_campeao > 90:
        print("\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###")
        print("Uma aura de destruição toma conta, não há escapatória.")
        print("Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!")
    else:
        print("\nItadori vence com honra e bravura!")