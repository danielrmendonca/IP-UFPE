print("Bem-vindo à missão dos duendes! Vamos construir o trenó mágico do Papai Noel!")
print("Quantos materiais mágicos estão trancados nos baús?")
print("Vamos começar desbloqueando os materiais!")

qtd_material = int(input())
ordem_material = 0
descobertos = 0
contador = 0

while ordem_material <= qtd_material:
    contador += 1
    print(f"Material {contador} de {qtd_material}")
    nome_item = str(input())
    tamanho = len(nome_item)

    if tamanho <= 5:
        tentativas = 7
    elif tamanho <= 10:
        tentativas = 9
    elif tamanho <= 13:
        tentativas = 13
    else: tentativas = 16

    forca = ""
    for caractere in nome_item:
        if caractere == " ":
            forca += " "
        else: forca += "_"
    print(forca)

    letras_chutes = ""
    acertou = False

    while tentativas > 0:
        letra = str(input())
        repetida = False
        letras_faltando = len(forca)

        for letra in letras_chutes:
            if letra in letras_chutes:
                repetida = True
        
        if repetida == True:
            print("") #nao sei
        else:
            letras_chutes += letra
            ordem_letra = 0
            posicoes = ""
        
            for i in range (1, (tamanho)+1):
                for chute in nome_item:
                    if letra == chute:
                        posicoes += str(i)
                        acertou = True
                        letras_faltando -=1

        if acertou == True:
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
    else:
        print(f"Você não conseguiu desbloquear o material. O nome correto era '{nome_item}'.")