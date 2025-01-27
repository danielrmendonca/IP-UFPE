vilões = []

entrada = input()

if entrada == "Novo vilão - Muito Perigodo":
    vilões.insert(0, input())

elif entrada == "Novo vilão - Meio perigoso":
    vilões.append(input())

elif entrada == "O que ele está fazendo aqui?":
    vilões.remove(input())

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
    print(", ".join(map(str, vilões)))

elif entrada == "Já temos nossa lista de vilões":
    lista_final = (", ".join(map(str, vilões)))
    print(f"O resultado final ficou assim: {lista_final}")