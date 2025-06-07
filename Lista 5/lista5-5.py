def buscar_palavra(matriz, palavra, linha, coluna, posicao, direcoes, visitados):
    encontrou = False

    if posicao == len(palavra):
        encontrou = True
    
    elif (linha<0 or linha>=len(matriz) or coluna<0 or coluna>=len(matriz[0])):
        encontrou = False 

    elif matriz[linha][coluna] != palavra[posicao]:
        encontrou = False    

    elif visitados[linha][coluna]:
        encontrou = False    
    
    else:
        visitados[linha][coluna] = True
    
        for deslocamento_linha, deslocamento_coluna in direcoes:
            if buscar_palavra(matriz, palavra, linha + deslocamento_linha, coluna + deslocamento_coluna, posicao + 1, direcoes, visitados):
                encontrou = True
                break

        visitados[linha][coluna] = False

    return encontrou

def encontrar_lugar(matriz, lugares):
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    lugares_formatados = [lugar.replace(" ", "").upper() for lugar in lugares]

    visitados = []
    for i in range (len(matriz)):
        linha_visitados = []
        for j in range (len(matriz[0])):
            linha_visitados.append(False)
        visitados.append(linha_visitados)
    
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            for indice in range(len(lugares_formatados)):
                lugar = lugares_formatados[indice]
                if buscar_palavra(matriz, lugar, l, c, 0, direcoes, visitados):
                    return lugares[indice]
    return

entrada = int(input())
matriz = [input().split() for _ in range(entrada)]
lugares = ["Penguin Bar", "Praia Gelada", "PenguiCup Stadium", "Delegacia Polar", "SubzeroWay", "Frio de Janeiro"]
lugar_encontrado = encontrar_lugar(matriz, lugares)

if lugar_encontrado == "Delegacia Polar":
    print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
elif lugar_encontrado == "Frio de Janeiro":
    print("ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
elif lugar_encontrado:
    print(f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {lugar_encontrado}. Vamos salvar nosso Carnaval de Inverno!")
else:
    print("Nosso carnaval de inverno está perdido... NÃOOOOO")