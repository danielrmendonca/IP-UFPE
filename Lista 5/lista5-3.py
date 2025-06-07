def derivada_monomios (polinomio):
    termos = polinomio.replace("-", "+-").split("+")
    resultado = []

    for termo in termos: #termo = ax^n
        if "x" not in termo:
            continue #derivada das constantes = 0
        if "^" in termo:
            coeficiente, expoente = termo.split("x^")
            if coeficiente:    
                if coeficiente == "-":
                    coeficiente = -1
                else:
                    coeficiente = int(coeficiente)
            else:
                coeficiente = 1
            expoente = int(expoente)

            coeficiente_derivado = coeficiente * expoente
            expoente_derivado = expoente - 1

            if expoente_derivado == 1:
                resultado.append(f"{coeficiente_derivado}x")
            else:
                resultado.append(f"{coeficiente_derivado}x^{expoente_derivado}")
        else:
            coeficiente = termo[:-1]
            if coeficiente:
                if coeficiente == "-":
                    coeficiente = -1
                else:
                    coeficiente = int(coeficiente)
            else:
                coeficiente = 1
            resultado.append(str(coeficiente))
        
    return "+".join(resultado).replace("+-", "-").strip() if resultado else "0"

def derivada (polinomio, ordem):
    if "x" not in polinomio:
        return "0"
    if ordem == 1:
        return derivada_monomios(polinomio)
    return derivada (derivada_monomios(polinomio), ordem-1)

polinomio = input()
ordem = int(input())

derivada_ordem_n = derivada(polinomio, ordem)

print(f"A derivada de ordem {ordem} da função {polinomio} é:\n{derivada_ordem_n}")