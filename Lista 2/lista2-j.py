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
    
    
    acertou_meterial = False

    while tentativas > 0 and letras_faltando > 0:
        letra = str(input())
        repetida = False
        acertou = False

        if letra in letras_chutadas:
                repetida = True

        else:
            ordem_letra = 0
            posicoes = ""

            if letra in nome_item:
                acertou = True
                letras_chutadas += letra
                
                for i in nome_item:
                    if i == letra:
                        posicoes += str(i)
                        letras_faltando -= len(posicoes)
        
        if repetida == True:
            tentativas -=1 

        elif acertou == True:
            if len(posicoes) > 1:
                aparicoes = "vezes"
            else: aparicoes = "vez"
            print(f"Acertamos uma letra! Ela aparece um total de {len(posicoes)} {aparicoes} na senha")

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

for i in range (1, qtd_partes+1):
    ordem_parte = i
    sequencia = str(input())+" "
    numero = ""
    maior = 0
    menor = 99999999999
    tentativas = 2
    partes_montadas = 0

    for caractere in sequencia:
        if caractere != " ":
            numero += caractere
        else:
            if int(numero) > maior:
                maior = int(numero)
                numero = ""
            elif int(numero) < menor:
                menor = int(numero)
                numero = ""

    resposta = int(maior + menor)

    while tentativas > 0:
        tentativa = int(input)
        if tentativa == resposta:
            print(f"Você decifrou o código da parte {ordem_parte}! O trenó está mais próximo de ficar completo!")
            partes_montadas += 1
        elif tentativas > 0:
            print("Número incorreto! Tente novamente.")
        else:
            print(f"Você não conseguiu decifrar o código. O número mágico era {resposta}.")

print(f"Você montou {partes_montadas} de {qtd_partes} partes do trenó!")
if partes_montadas == qtd_partes:
    print("Parabéns! O trenó está completo e pronto para voar!")
elif partes_montadas >= (qtd_partes // 2):
    print("Bom trabalho! O trenó quase ficou completo!")
else: print("Parece que o trenó ficou incompleto. Tente novamente na próxima missão!")
