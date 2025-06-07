lideres = {}
acontecimentos = {}
comando = ""
while comando != "FIM":
    comando = input()
    if comando != "FIM":
        if comando == "REGISTRAR LÍDER":
            nome = input()
            cargo = input()
            cidade = input()
            data = input()

            lideres[nome] = (cargo, cidade, data)
        else:
            data = input()
            acontecimento = input()
            local = input()

            acontecimentos[data] = (acontecimento, local)

if lideres:
    print("Consegui encontrar os seguintes líderes da Revolução Pernambucana de 1817:")
    for lider in lideres:
        print(lider+":")
        cargo, cidade, data = lideres[lider]
        print(f"- Cargo/Papel: {cargo}")
        print(f"- Cidade de Origem: {cidade}")
        print(f"- Data de Nascimento: {data}")
else:
    print("Aff, pelo jeito nessa época não tinha LinkedIn pra facilitar encontrar os tais líderes dessa tal Revolução... Desisto.")
print()
if acontecimentos:
    print("Vivenciei os seguintes acontecimentos históricos da Revolução Pernambucana de 1817:")
    for dia in acontecimentos:
        acontecimento, local = acontecimentos[dia]
        print(f"({dia}): {acontecimento}, {local}")
else:
    print("Ter que ler todos esses jornais não é legal, e ainda não encontrei nenhum acontecimento... saudade do Pernambuco Extraordinário pra me manter informado.")

if lideres and acontecimentos:
    print("\nPronto, agora CIn tô preparado pra lutar e tornar Pernambuco o melhor país em linha reta do mundo!!!")