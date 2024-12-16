altura = int(input())
altura_total = 2*altura-1 
espaco = "⠀"

for i in range (1, (altura_total)+1):
    if i == 1 or i == altura_total + 1:
        for espaco_esquerda in range (altura-i):
            print(espaco, end="")
        print("*", end="")
        for espaco_direita in range (altura-i):
            print(espaco, end="")
    elif i == altura:
        for a in range (altura-1):
            print(("*"+espaco), end="")
            print("*")
    else:
        if i<altura:
            for espaco_esquerda in range (altura-i):
                print(espaco, end="")
            print("*", end="")
            for espaco_central in range ((2*i) -3):
                print(espaco, end="")
            print("*", end="")
            for espaco_direita in range (altura-i):
                print(espaco)

        elif i > altura:
            for espaco_esquerda in range ((altura-i) *-1):
                print(espaco, end="")
            print("*", end="")
            for espaco_central in range ():#nao sei
                print(espaco, end="")
            print("*", end="")
            for espaco_direita in range (altura-i):
                print(espaco)