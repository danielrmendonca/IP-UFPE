alianca_nordestina = {
    "estados": ["PE", "PB", "RN", "CE", "AL", "BA"],
    "vida": 1000,
    "riqueza": 20000,
    "soldados": 100000,
    "vitorias": 0,
    "derrotas": 0,
    "anexados": []
}

coroa_portuguesa = {
    "estados": ["SP", "RJ", "ES", "MG", "PR", "RS"],
    "vida": 1000,
    "riqueza": 20000,
    "soldados": 100000,
    "vitorias": 0,
    "derrotas": 0,
    "anexados": []
}

armas = {
    "Mosquete": 7000,
    "Baioneta": 3000,
    "Canhão": 10000,
    "Espada": 3500,
    "Pederneira": 5000
}

estados_vantagem = [ "PE", "PB", "RN"]

def calcular_forca(dinheiro, soldados, lista):
    letalidade_total = armas[lista[0]] + armas[lista[1]] + armas[lista[2]]
    forca = ((dinheiro * 2) + (soldados * 4) + (letalidade_total) * 4) / 10
    return forca

def turno(forca_atacante, forca_defensor): #continuar
    if forca_atacante > forca_defensor:
        vencedor = estado_atacante
    elif forca_atacante < forca_defensor:
        vencedor = estado_defensor
    else:
        vencedor = ""
    return vencedor

def processar_batalha(vida, forca_vencedor, forca_perdedor, bloco_vencedor, estado_perdedor, bloco_perdedor):
    dano = vida * (1 - forca_perdedor / forca_vencedor)
    vida -= dano
    
    bloco_perdedor["estados"].remove(estado_perdedor)
    bloco_vencedor["anexados"].append(estado_perdedor)

def verificar_arma(arma, armas):
    if arma in armas:
        return True
    else:
        print("@ selecione uma arma válida! @")
        return False
    
def adicionar_arma(armas):
    armas_batalha = []
    while len(armas_batalha) < 3:
        arma = input()
        if verificar_arma(arma, armas):
            armas_batalha.append(arma)
        return armas_batalha

def verificar_estado(estado, estados):
    if estado not in estados["estados"]:
        return False
    else:
        return True

##########       MAIN       ##############
for batalha in range (1, 4):

    estado_atacante = input()
    while not verificar_estado(estado_atacante):
        print("@ estado não encontrado ou não faz parte das regiões em guerra! @")
        estado_atacante = input()

    dinheiro_atacante = int(input())
    soldados_atacante = int(input())
    armas_batalha_atacante = adicionar_arma(armas)

    estado_defensor = input()
    while not verificar_estado(estado_defensor):
        print("@ escolha um estado válido para contra-atacar! @")
        estado_defensor = input()

    dinheiro_defensor = int(input())
    soldados_defensor = int(input())
    armas_batalha_defensor = adicionar_arma(armas)

    if estado_atacante in estados_vantagem:
          print(f"o estado de {estado_atacante} ganhou 10% de força pois está lutando em um campo de batalha que lhe confere vantagem!")
    
    if estado_atacante in alianca_nordestina["estados"]:
        alianca_nordestina["riqueza"] -= dinheiro_atacante
        alianca_nordestina["soldados"] -= soldados_atacante
        coroa_portuguesa["riqueza"] -= dinheiro_defensor
        coroa_portuguesa["soldados"] -= soldados_defensor
    else:
        alianca_nordestina["riqueza"] -= dinheiro_defensor
        alianca_nordestina["soldados"] -= soldados_defensor
        coroa_portuguesa["riqueza"] -= dinheiro_atacante
        coroa_portuguesa["soldados"] -= soldados_atacante

    forca_atacante = calcular_forca(dinheiro_atacante, soldados_atacante, armas_batalha_atacante)
    forca_defensor = calcular_forca(dinheiro_defensor, soldados_defensor, armas_batalha_defensor)

    