quantidade_folhas = int(input())
populacao = int(input())
altura = int(input())

if altura < 2:
    print("Isso não é uma árvore, é um arbusto!")
else:
    folhas_arvore = 0
    for i in range (altura+1):
        folhas_arvore += i*2
    if folhas_arvore > quantidade_folhas:
        print("Infelizmente não poderemos comemorar o Natal esse ano, não conseguimos fazer uma única árvore!")
    else:
        arvores_possiveis = 0
        folhas_restantes = quantidade_folhas

        while folhas_restantes >= folhas_arvore:
            folhas_restantes -= folhas_arvore
            arvores_possiveis += 1
        
        for i in range (altura+1):
            espacos = "⠀" * (altura - i + 1)
            if i == 0:
                print(espacos + "*")
            else:
                print(espacos + (i * "+") + "⠀" + (i * "+"))
            
        if arvores_possiveis >= populacao:
            print("O Grinch não conseguiu estragar o Natal dessa vez!")
        else: print("Essa árvore está muito grande, dessa forma não conseguiremos entregar para a cidade toda")