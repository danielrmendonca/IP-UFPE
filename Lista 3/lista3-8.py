entrada = input().split("-")
sequencia_gojo = list(map(int, entrada))

maior_seq_geto = int(input())
soma_geto = int(input())

maior_seq_gojo = []
parcial = []

for i in sequencia_gojo:
    if not parcial or parcial[-1] == i-1:
        parcial.append(i)
    else:
        if len(parcial) > len(maior_seq_gojo):
            maior_seq_gojo = parcial
        parcial = [i]

if len(parcial) > len(maior_seq_gojo):
    maior_seq_gojo = parcial

if len(maior_seq_gojo) > maior_seq_geto:
    print("Uma vitória avassaladora de Satoru Gojo. Nem mesmo o infinito pode pará-lo. Ele realmente é o melhor!")
elif maior_seq_geto > len(maior_seq_gojo):
    print("Inesperado! Suguru Geto domina com maestria. Uma vitória indiscutível!")
elif len(maior_seq_gojo) == maior_seq_geto:
    soma_gojo = sum(maior_seq_gojo)
    if soma_gojo > soma_geto:
        print("Gojo vence por pouco. Mesmo com toda a pressão, ele continua no topo!")
    elif soma_geto > soma_gojo:
        print("Geto vence por pouco. Sua estratégia foi impecável nesta batalha!")
    else:
        print("Um empate absoluto! Quem diria que duas lendas podem ser tão iguais em poder?")