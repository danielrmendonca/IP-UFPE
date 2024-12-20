print("Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!")
print("Quantos materiais mágicos estão trancados nos baús?")
print("Vamos começar desbloqueando os materiais!")

qtd_material = int(input())
ordem_material = 0
descobertos = 0

for i in range (1, qtd_material+1):
    ordem_material += 1
    print(f"Material {ordem_material} de {qtd_material}")
    nome_item = str(input())
    tamanho = len(nome_item)

    if tamanho <= 5:
        tentativas = 7
    elif tamanho <= 10:
        tentativas = 9
    elif tamanho <= 13:
        tentativas = 13
    else: tentativas = 16

    letras_faltando = 0
    forca = ""
    for caractere in nome_item:
        if caractere == " ":
            forca += " "
        else:
            forca += "_"
            letras_faltando += 1
        
    print(f"Senha mágica: {forca}")

    letras_chutadas = ""

    while tentativas > 0 and letras_faltando > 0:
        letra = str(input())
        repetida = False
        acertou = False

        if letra in letras_chutadas:
                repetida = True

        else:
            ordem_letra = 0

            if letra in nome_item:
                acertou = True
                letras_chutadas += letra
                
                contador_letras_palavra = 0

                for l in nome_item:
                    if l == letra:
                        contador_letras_palavra += 1

                    
                letras_faltando -= contador_letras_palavra
        
        if repetida == True:
            tentativas -=1 
            if tentativas == 0:
                print("Infelizmente não conseguimos descobrir a senha.")

        elif acertou == True:
            tentativas -= 1
            if contador_letras_palavra > 1:
                aparicoes = "vezes"
            else: aparicoes = "vez"
            print(f"Acertamos uma letra! Ela aparece um total de {contador_letras_palavra} {aparicoes} na senha")

        else:
            tentativas -= 1
            if tentativas > 0:
                print("Erramos a letra! Porém ainda temos mais tentativas.")
            else: print("Infelizmente não conseguimos descobrir a senha.")

    
    if letras_faltando == 0:
        print(f"Parabéns! Você desbloqueou o material mágico '{nome_item}'!")
        descobertos += 1
    else:
        print(f"Você não conseguiu desbloquear o material. O nome correto era '{nome_item}'.")

print(f"Você desbloqueou {descobertos} de {qtd_material} materiais mágicos!")
print(f"Os duendes precisam decifrar os códigos perdidos para montar o trenó!")
print(f"Quantas partes o trenó possui?")

ordem_parte = 1
qtd_partes = int(input())
partes_montadas = 0

for p in range (1, qtd_partes+1):
    ordem_parte = p
    sequencia = input()+" "
    numero = ""
    maior = 0
    menor = 0
    primeiro_numero = True
    tentativas = 2
    print(f"Parte {ordem_parte} de {qtd_partes}")

    for caractere in sequencia:
        if caractere != " ":
            numero += caractere
        else:
            if primeiro_numero == True:
                maior = int(numero)
                menor = int(numero)
                primeiro_numero = False
            else:
                if int(numero) > maior:
                    maior = int(numero)
                if int(numero) < menor:
                    menor = int(numero)
            numero = ""

    print(f"Dica: O menor número é {menor} e o maior número é {maior}.")

    resposta = int(maior + menor)
    parte_atual = False
    break_while = False

    while parte_atual == False and break_while == False:
        
        print(f"Descubra o número mágico (soma de {menor} e {maior})")
        tentativa = int(input())
        if tentativa == resposta:
            print(f"Você decifrou o código da parte {ordem_parte}! O trenó está mais próximo de ficar completo!")
            partes_montadas += 1
            parte_atual = True
        elif tentativas == 2:
            print("Número incorreto! Tente novamente.")
            tentativas -= 1
        elif tentativas == 1:
            tentativas -= 1
            print("Número incorreto! Tente novamente.")
            break_while = True

    if tentativas == 0:
            print(f"Você não conseguiu decifrar o código. O número mágico era {resposta}.")

print(f"Você montou {partes_montadas} de {qtd_partes} partes do trenó!")
if partes_montadas == qtd_partes:
    print("Parabéns! O trenó está completo e pronto para voar!")
elif partes_montadas >= (qtd_partes // 2):
    print("Bom trabalho! O trenó quase ficou completo!")
else: print("Parece que o trenó ficou incompleto. Tente novamente na próxima missão!")
