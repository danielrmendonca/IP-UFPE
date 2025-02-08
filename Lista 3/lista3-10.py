nome_feiticeiro = input()
vida_feiticeiro = int(input())
ataque_feiticeiro = int(input())
defesa_feiticeiro = int(input())
reversao_feitico_str = input()
if reversao_feitico_str == "True":
    reversao_feitico = True
else:
    reversao_feitico = False
expansao_dominio_str = input()
if expansao_dominio_str == "True":
    expansao_dominio = True
else:
    expansao_dominio = False

vida_mahogara = int(input())
ataque_mahogara = int(input())
defesa_mahogara = int(input())

lista_golpes_feiticeiro = input().split(", ")
lista_golpes_mahogara = ["ataque", "regeneração", "adaptação"]

golpes_usados = []
golpes_adaptados = []

golpes_registrados_adaptacao = []
adaptacoes = []

if not reversao_feitico:
    print("Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!")
else:
    print("Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!")

luta_finalizada = False
turno_feiticeiro = True

while not luta_finalizada:
    if turno_feiticeiro:
        golpe = input()

        if golpe == "reversão de feitiço":
            if reversao_feitico:
                print("Eu posso continuar lutando mais um pouco...")
                vida_feiticeiro += 25
            turno_feiticeiro = False

        elif golpe == "expansão de domínio":
            if not expansao_dominio:
                print("Droga. Eu não aprendi a expandir meu domínio ainda!")
            else:
                if nome_feiticeiro == "Satoru Gojo":
                    print(f"Como assim o Mahoraga já se adaptou ao infinito de {nome_feiticeiro}!?")
                else:
                    print("Nem mesmo a sua adaptação pode derrotar isto!")
                    vida_mahogara = 0
                    luta_finalizada = True
            turno_feiticeiro = False

        elif golpe == "black flash":
            print("As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!")
            dano = (ataque_feiticeiro + 25)*2
            vida_mahogara -= dano
            turno_feiticeiro = False

        elif golpe not in lista_golpes_feiticeiro: #golpe desconhecido
            print("Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!")
            turno_feiticeiro = False

        else: #golpe conhecido diferente de reversao, expansão ou black flash
            dano = ((ataque_feiticeiro-defesa_mahogara)+25)
            if golpe not in golpes_usados:
                vida_mahogara -= dano
                golpes_usados.append(golpe)
            elif golpe in golpes_adaptados:
                print("Esse ataque é inútil! Melhor tentar outra coisa.")
            else: #golpe não adaptado e que já foi usado
                indice = golpes_registrados_adaptacao.index(golpe)
                if adaptacoes[indice] == 1:
                    dano = dano/2
                elif adaptacoes[indice] == 2:
                    dano = dano/4
                elif adaptacoes[indice] == 3:
                    dano = 0
                vida_mahogara -= dano

            if golpe not in golpes_adaptados: #golpe não adaptado sendo usado pela primeira vez ou não
                if golpe not in golpes_registrados_adaptacao:
                    golpes_registrados_adaptacao.append(golpe) #lista paralelas para contar as adaptações
                    adaptacoes.append(1) #lista para contar as adaptações
                    print(f"A roda do Mahoraga girou uma vez! {golpe} só vai funcionar mais duas vezes")
                else: #segunda vez ou mais do golpe
                    indice = golpes_registrados_adaptacao.index(golpe)
                    adaptacoes[indice] += 1 #conta a adaptação
                    if adaptacoes[indice] == 2:
                        print(f"A roda do Mahoraga girou pela segunda vez! {golpe} só vai funcionar mais uma vez")
                    elif adaptacoes[indice] == 3:
                        golpes_adaptados.append(golpe)
                        print(f"A roda do Mahoraga girou pela terceira vez! {golpe} não vai funcionar mais")
            if len(golpes_adaptados) == len(lista_golpes_feiticeiro):
                print("Droga... Eu não tenho mais nada para usar contra o Mahoraga.. Essa luta acabou.")
                luta_finalizada = True
            turno_feiticeiro = False
    if vida_mahogara <= 0 or vida_feiticeiro <= 0:
        break
    
    else:
        golpe_mahogara = input()
        if golpe_mahogara not in lista_golpes_mahogara:
            turno_feiticeiro = True
            continue
        else:
            if golpe_mahogara == "ataque":
                dano = ((ataque_mahogara-defesa_feiticeiro)+25)
                vida_feiticeiro -= dano
                turno_feiticeiro = True

            elif golpe_mahogara == "regeneração":
                print("Ele está se regenerando.")
                vida_mahogara += 25
                turno_feiticeiro = True

            elif golpe_mahogara == "adaptação":
                if golpes_usados:    
                    ultimo_golpe = golpes_usados[-1]
                    if ultimo_golpe == "black flash": #não precisa se preocupar com reversão
                        print("Nem você vai conseguir se adaptar a isso, mahoraga!")
                    else:
                            indice = golpes_registrados_adaptacao.index(ultimo_golpe)
                            adaptacoes[indice] += 1
                            if adaptacoes[indice] == 2:
                                print(f"A roda do Mahoraga girou pela segunda vez! {ultimo_golpe} só vai funcionar mais uma vez")
                            elif adaptacoes[indice] == 3:
                                golpes_adaptados.append(ultimo_golpe)
                                print(f"A roda do Mahoraga girou pela terceira vez! {ultimo_golpe} não vai funcionar mais")
                                
            if len(golpes_adaptados) == len(lista_golpes_feiticeiro):
                                print("Droga... Eu não tenho mais nada para usar contra o Mahoraga.. Essa luta acabou.")
                                luta_finalizada = True
    if vida_feiticeiro <= 0:
        luta_finalizada = True
if vida_mahogara <= 0:
    print(f"{nome_feiticeiro} conseguiu!")
    if nome_feiticeiro == "Megumi Fushiguro":
        print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!")
    elif nome_feiticeiro == "Sukuna":
        print("Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!")
    elif nome_feiticeiro == "Satoru Gojo":
        print("Nem você sua adaptação é páreo para o infinito, queridinho.")
    else:
        print("Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.")
    luta_finalizada = True
elif vida_feiticeiro <= 0 or vida_mahogara > 0 and vida_feiticeiro > 0:
    if nome_feiticeiro == "Satoru Gojo":    
        print("Magnífico, Satoru Gojo. Lembrarei de você enquanto eu durar nesta vida.")
    else:
        print(f"Parece que nem mesmo {nome_feiticeiro} foi pareo contra o Mahoraga...")
