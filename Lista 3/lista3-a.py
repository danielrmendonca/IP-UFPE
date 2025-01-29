vilões = []
entrada = ""

while entrada != "Já temos nossa lista de vilões":
    entrada = input()
    if entrada == "Novo vilão - Muito Perigoso":
        vilao_perigoso = input()
        vilões.insert(0, vilao_perigoso)

    elif entrada == "Novo vilão - Meio perigoso":
        vilao_mperigoso = input()
        vilões.append(vilao_mperigoso)

    elif entrada == "O que ele está fazendo aqui?":
        vilao_remover = input()
        vilões.remove(vilao_remover)

    elif entrada == "Vilão mais perigoso do que pensávamos":
        atual = int(input())
        novo = int(input())
        vilões[atual], vilões[novo] = vilões[novo], vilões[atual]

    elif entrada == "Que estranho, esses dois vilões… troque-os de lugar":
        vilao_1 = input()
        vilao_2 = input()
        indice_1 = vilões.index(vilao_1)
        indice_2 = vilões.index(vilao_2)
        vilões[indice_1], vilões[indice_2] = vilões[indice_2], vilões[indice_1]

    elif entrada == "Essa posição não está de acordo, ele nem odeia carecas":
        vilao_final = input()
        vilões.remove(vilao_final)
        vilões.append(vilao_final)

    elif entrada == "Como a lista está ficando?":
        lista_parcial = (", ".join(vilões))
        print(lista_parcial)

    elif entrada == "Já temos nossa lista de vilões":
        lista_final = (", ".join(vilões))
        print(f"O resultado final ficou assim:\n{lista_final}")
