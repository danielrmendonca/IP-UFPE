def maior_lista (numeros, k, indice=0, atual=0, maior=0):
    if atual == 0:
        atual = []
    if maior == 0:
        maior = []

    if sum(atual) == k:
        if len(atual) >= 4 and len(atual) > len(maior):
            maior = atual

    if indice >= len(numeros):
        return maior
    
    incluir = maior_lista(numeros, k, indice+1, atual+[numeros[indice]])
    excluir = maior_lista(numeros, k, indice+1, atual)

    if len(incluir) > len(excluir):
        return incluir
    else:
        return excluir


def formatar_senha(lista, indice=0, senha=""):
    if indice >= len(lista):
        if len(senha) >= 4:
            return senha
        else:
            return
    
    numero_formatado = str(abs(lista[indice])).replace("0", "")
    return formatar_senha (lista, indice+1, senha+numero_formatado)
        
def processar_portas():  
    criptografia = list(map(int, input().split(", ")))
    k = int(input())
    entrada.append((criptografia, k))
    
    numeros = entrada[porta][0]
    k = entrada[porta][1]

    maior_lista_encontrada = maior_lista(numeros, k)

    if not maior_lista_encontrada:
        print("Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!")
        return True
    
    senha = formatar_senha(maior_lista_encontrada)

    if senha:
        print(f"A senha da porta {porta+1} é: {senha}")
    else:
        print("Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!")
        return True
        
portas = int(input())
entrada = []
for porta in range (portas):
    if processar_portas():
        break