presente = 0
boneco = 0
bicicleta = 0
videogame = 0
outros = 0

while presente != "FIM":
    presente = str(input())
    if presente != "FIM":
        if presente == "Boneco":
            print("Mais um presente saindo!")
            boneco += 1
        elif presente == "Videogame":
            print("Mais um presente saindo!")
            videogame += 1
        elif presente == "Bicicleta":
            print("Mais um presente saindo!")
            bicicleta +=1
        else:
            print("Esse presente não está sendo fabricado nesse momento")
            outros += 1
print("Vamos agora ao relatório dos presentes!")

total_presentes = int(boneco) + int(videogame) + int(bicicleta) + int(outros)
p_boneco = (boneco / total_presentes) * 100 
p_videogame = (videogame / total_presentes) * 100
p_bicicleta = (bicicleta / total_presentes) * 100
p_outros = (outros / total_presentes) * 100

print(f"Boneco - {boneco} unidades - {p_boneco:.2f}%")
print(f"Videogame - {videogame} unidades - {p_videogame:.2f}%")
print(f"Bicicleta - {bicicleta} unidades - {p_bicicleta:.2f}%")
print(f"Outros - {outros} unidades - {p_outros:.2f}%")

if outros == 0:
    print('A demanda está muito alta! Teremos que fazer mais uma fábrica!')
elif p_outros > 50:
    print('Parece que o Papai Noel terá que fechar a fábrica :(')
elif p_outros <= 50 and p_bicicleta <= 50 and p_boneco <= 50 and p_videogame <= 50:
    print('A fábrica está cumprindo seu papel, porém não precisa ser expandida')
else:
    if p_boneco > 50:
        print ('Boneco está sendo muito desejado! A fábrica terá que ser expandida!')
    elif p_bicicleta > 50:
        print('Bicicleta está sendo muito desejado! A fábrica terá que ser expandida!')
    else: print('Videogame está sendo muito desejado! A fábrica terá que ser expandida!')