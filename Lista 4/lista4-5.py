def zap (defesa, vida, velocidade):
    if not defesa:
        vida -= 5
    velocidade -= 1
    return vida, velocidade

def powpow (defesa, vida):
    if not defesa:
        vida -= 15
    return vida

def fishbones(defesa, vida):
    if not defesa:
        vida-= 30
    else:
        defesa = False
    return defesa, vida

def lanca_missil (defesa, vida, missil_disponivel):
    if missil_disponivel:
        if not defesa:
            vida -= 100
    missil_disponivel = False
    return vida, missil_disponivel

def arma (distancia, defesa, missil_disponivel):
    if defesa:
        if distancia >= 30:
            return "fishbones"
        else:
            return "zap"
    else:
        if distancia >= 50:
            if missil_disponivel:
                return "lanca_missil"
            else:
                return "fishbones"
        elif distancia >= 30:
            return "fishbones"
        elif distancia >= 15:
            return "powpow"
        else:
            return "zap"
        
entrada = input().split(" - ")
nome = entrada[0]
vida = int(entrada[1])
distancia = int(entrada[2])
velocidade = int(entrada[3])
if entrada[4] == "0":
    defesa = False
else: defesa = True
missil_disponivel = True

print(f"Andando pelas ruas de Zaun, jinx dá de cara com um {nome} e agora vão lutar.")
while vida>0 and distancia >0:
    arma_escolhida = arma(distancia, defesa, missil_disponivel)
    if distancia >= 30:
        if arma_escolhida == "zap":
            print("Você foi zapeado hahaha.")
            vida, velocidade = zap (defesa, vida, velocidade)
        elif arma_escolhida == "powpow":
            print("Jinx vai encher esse cara de buracos agora.")
            vida = powpow (defesa, vida)
        elif arma_escolhida == "fishbones":
            if defesa:
                print("A defesa dele foi destruída com o poder da Fishbones!")
            else:
                print("Vamos derretê-lo com a Fishbones!")
            defesa, vida = fishbones(defesa, vida)

        elif arma_escolhida == "lanca_missil":
            print("Ele vai ser transformado em cinzas pelo SUPER MÍSSIL!")
            vida, missil_disponivel = lanca_missil (defesa, vida, missil_disponivel)
    else:
        if defesa:
            if arma_escolhida == "zap":
                print("Ele está com defesa e está muito perto!")
                vida, velocidade = zap (defesa, vida, velocidade)
        else:
            if arma_escolhida == "zap":
                print("Você foi zapeado hahaha.")
                vida, velocidade = zap (defesa, vida, velocidade)
    distancia -= velocidade
    if vida <= 0:
        print("Ninguem é capaz de derrotar a Jinx!!!")
    elif distancia <= 0:
        print("Ah não, A Jinx foi PEGA!")