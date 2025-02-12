estados_existentes = int(input())
if estados_existentes == 1:
    print("É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(")
else:
    estados = []
    for i in range (1, estados_existentes+1):
        estados.append(f"q{i}")

    estado_final = input()
    conexoes = []
    for a in range (estados_existentes):
        conexoes.append = input().replace("-", "->")
    
    cadeias_binarias = int(input())
    cadeias = []
    for b in range (cadeias_binarias):
        cadeia = input()
        estado0 = input()
        cadeias.append(cadeia, estado0)
        
    for c in conexoes:
            print(f"{estados[c]}: {{{conexoes[c]}}}")
    
    bits = ["0", "1", "ε"]
    #estados = lista com todos os estados
    #estado_final = estado aceitação onde deve terminar o deslocamento
    for d in range (cadeias_binarias):
         estado_atual = cadeias[d][1]
         for caractere in cadeias[d][0]:
              if caractere == "ε":
                   if cadeias[d][1] == estado_final:
                        print("Caramba, essa cadeia é abençoada! Nem precisei trabalhar!")
                   else:
                        print("Nossa, que maldição! Nem começou e já deu errado…")
                        break
              elif caractere not in bits:
                   print(f"Só pode estar de brincadeira comigo! Como vou lidar com {caractere} dentro da máquina?")
                   break
              else:
                   if estado_atual == cadeias[d][1]:
                        print("Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!")
                   else:
                        print("Que tristeza, todo esse arrudeio pra nada…")