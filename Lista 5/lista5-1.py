def pertencimento (n, termo1=0, termo2=1):
    pertence = False
    if n == termo1 or n == termo2:
        pertence = True
    else:
        if termo2 <= maximo:
            return pertencimento(n, termo2, termo1+termo2)
    return pertence

qtd_numeros = int(input())
entrada = []
for numero in range (qtd_numeros):
    numero = int(input())
    entrada.append(numero)
maximo = max(entrada)
pertencentes = [n for n in entrada if pertencimento(n)]

print(f"Contei um total de {len(pertencentes)} números que estão na sequência de penguinacci!")

if len(pertencentes) == len(entrada):
    print(f"Boa, Paulo! Todos esses números fazem parte da sequência de penguinacci.")
elif len(pertencentes) > 0:
    print("Eita, nem todos que você falou fazem parte da sequência de penguinacci. Os que fazem parte são:")
    print(", ".join(str(termo) for termo in sorted(pertencentes)))
else: print("Acho que é melhor revisar a teoria um pouco...")