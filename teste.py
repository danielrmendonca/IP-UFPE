def busca_palavra(matriz, palavra, linha, coluna, posicao, direcoes):
    # Verifica se a palavra foi encontrada completamente
    if posicao == len(palavra):
        return True
    
    # Verifica se está fora dos limites da matriz ou se o caractere não coincide
    if (linha < 0 or linha >= len(matriz) or 
        coluna < 0 or coluna >= len(matriz[0]) or 
        matriz[linha][coluna] != palavra[posicao]):
        return False
    
    # Marca a posição atual como visitada
    temp = matriz[linha][coluna]
    matriz[linha][coluna] = '#'
    
    # Busca recursiva em todas as direções
    for dir_linha, dir_coluna in direcoes:
        if busca_palavra(matriz, palavra, linha + dir_linha, coluna + dir_coluna, posicao + 1, direcoes):
            return True
    
    # Restaura o caractere original
    matriz[linha][coluna] = temp
    return False

def encontrar_lugar(matriz, lugares):
    # Define as direções possíveis (8 direções)
    direcoes = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
    
    # Remove espaços e converte para maiúsculas
    lugares_formatados = [lugar.replace(" ", "").upper() for lugar in lugares]
    
    # Percorre a matriz e tenta encontrar cada lugar
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for idx, lugar in enumerate(lugares_formatados):
                if busca_palavra(matriz, lugar, i, j, 0, direcoes):
                    return lugares[idx]  # Retorna o lugar original (com espaços)
    
    return None  # Se nenhum lugar for encontrado

# Entrada do usuário
entrada = int(input())
matriz = [input().split() for _ in range(entrada)]

# Lista de lugares
lugares = ["Penguin Bar", "Praia Gelada", "PenguiCup Stadium", 
           "Delegacia Polar", "SubzeroWay", "Frio de Janeiro"]

# Encontra o lugar na matriz
lugar_encontrado = encontrar_lugar(matriz, lugares)

# Exibe o resultado
if lugar_encontrado == "Delegacia Polar":
    print("Se formos até a Delegacia Polar, estaremos mexendo com um fora da lei. Vamos até lá investigar!")
elif lugar_encontrado == "Frio de Janeiro":
    print("ARRGH! Todos sabem que o melhor carnaval é no bloco Pinguim da Madrugada. Vamos buscar nossa estátua no Frio de Janeiro")
elif lugar_encontrado:
    print(f"Temos que correr! O Pinguim da Madrugada pode estar no(a) {lugar_encontrado}. Vamos salvar nosso Carnaval de Inverno!")
else:
    print("Nosso carnaval de inverno está perdido... NÃOOOOO")
