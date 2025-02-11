def consumo_energia (horas, potencia, ineficiencia):
    energia_inicial = potencia * horas
    return (energia_inicial + ((ineficiencia/100)*energia_inicial))

def dinheiro_gasto (preco_unidade, consumo_total):
    return (preco_unidade * consumo_total)

numero_maquinas = int(input())
custo_total = 0
maior_custo = 0
for maquina in range (numero_maquinas):
    H = int(input())
    P = float(input())
    I = int(input())
    G = float(input())
    consumo_total = consumo_energia(H, P, I)

    if consumo_total == 0:
        print("Parece que essa coisa nem ao menos funciona")
    elif consumo_total > 0 and consumo_total <= 100:
        print(f"Temos aqui uma máquina formidável, seu consumo de energia é {consumo_total:.2f}")
    elif consumo_total >100 and consumo_total <= 300:
        print(f"Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {consumo_total:.2f}")
    else:
        print("Você se importaria de jogar seus explosivos em qualquer outro lugar?")
    
    custo_maquina = dinheiro_gasto(G, consumo_total)
    custo_total += custo_maquina
    if custo_maquina > maior_custo:
        maior_custo = custo_maquina

print(f"Os gastos totais com as maquinas foi de {custo_total:.2f}")
print(f"A máquina mais cara gasta um total de {maior_custo:.2f} para os cofres de Piltover")
