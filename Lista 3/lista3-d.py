categoria_especial_o = []
nivel_1_o = []
nivel_2_o = []
nivel_3_o = []
nivel_4_o = []

categoria_especial_a = []
nivel_1_a = []
nivel_2_a = []
nivel_3_a = []
nivel_4_a = []

while True:
    tipo = input()
    if tipo == "Catalogação encerrada!":
        break
    else:
        if tipo == "objeto":
            item_classificacao_o = input()
            item_o, classificacao_o = item_classificacao_o.split(" - ")
            artigo = "O"
            genero = "catalogado"
            nome = item_o

            if classificacao_o == "0":
                categoria_especial_o.append(item_o)
            elif classificacao_o == "1":
                nivel_1_o.append(item_o)
            elif classificacao_o == "2":
                nivel_2_o.append(item_o)
            elif classificacao_o == "3":
                nivel_3_o.append(item_o)
            else: nivel_4_o.append(item_o)

        else:
            item_classificacao_a = input()
            item_a, classificacao_a = item_classificacao_a.split(" - ")
            artigo = "A"
            genero = "catalogada"
            nome = item_a

            if classificacao_a == "0":
                categoria_especial_a.append(item_a)
            elif classificacao_a == "1":
                nivel_1_a.append(item_a)
            elif classificacao_a == "2":
                nivel_2_a.append(item_a)
            elif classificacao_a == "3":
                nivel_3_a.append(item_a)
            else: nivel_4_a.append(item_a)
        
        print(f"{artigo} {tipo} {nome} foi {genero} com sucesso!")

print("Processando lista de itens…")
print()
print("ITENS AMALDIÇOADOS DA TOKYO JUJUTSU HIGH\n")
print("Objetos")

if len(categoria_especial_o) > 0:
    print(f"Categoria Especial: {', '.join(categoria_especial_o)}")
if len(nivel_1_o) > 0:
    print(f"Nível 1: {', '.join(nivel_1_o)}")
if len(nivel_2_o) > 0:
    print(f"Nível 2: {', '.join(nivel_2_o)}")
if len(nivel_3_o) > 0:
    print(f"Nível 3: {', '.join(nivel_3_o)}")
if len(nivel_4_o) > 0:
    print(f"Nível 4: {', '.join(nivel_4_o)}")

print("\nArmas")

if len(categoria_especial_a) > 0:
    print(f"Categoria Especial: {', '.join(categoria_especial_a)}")
if len(nivel_1_a) > 0:
    print(f"Nível 1: {', '.join(nivel_1_a)}")
if len(nivel_2_a) > 0:
    print(f"Nível 2: {', '.join(nivel_2_a)}")
if len(nivel_3_a) > 0:
    print(f"Nível 3: {', '.join(nivel_3_a)}")
if len(nivel_4_a) > 0:
    print(f"Nível 4: {', '.join(nivel_4_a)}")