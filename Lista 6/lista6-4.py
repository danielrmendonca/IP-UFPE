figuras_historicas = {
    "Zumbi dos Palmares": {"impacto": 0, "legado": 1000, "ramo": ""},
    "Frei Caneca": {"impacto": 0, "legado": 900, "ramo": ""},
    "Paulo Freire": {"impacto": 0, "legado": 800, "ramo": ""},
    "Clarice Lispector": {"impacto": 0, "legado": 800, "ramo": ""},
    "Ariano Suassuna": {"impacto": 0, "legado": 700, "ramo": ""},
    "Chico Science": {"impacto": 0, "legado": 600, "ramo": ""},
    "Luiz Gonzaga": {"impacto": 0, "legado": 500, "ramo": ""},
    "Eduardo Campos": {"impacto": 0, "legado": 400, "ramo": ""},
    "Rivaldo": {"impacto": 0, "legado": 300, "ramo": ""},
    "Lia de Itamaracá": {"impacto": 0, "legado": 200, "ramo": ""}
}

ordem_relevancia = {
    "Revolucionário": 1,
    "Líder comunitário": 2,
    "Cientista": 3,
    "Político": 4,
    "Escritor": 5,
    "Educador": 6,
    "Artista": 7,
    "Atleta": 8    
}

def processamento_bairros ():
    n = int(input())
    for bairro in range(n):
        nome_bairro = input()
        populacao = int(input())
        for podio in range(3):
            figura, ramo = input().split(" - ")

            if podio == 0:
                impacto = populacao
            elif podio == 1:
                impacto = populacao // 2
            else:
                impacto = populacao //3

            figuras_historicas[figura]["impacto"] += impacto
            figuras_historicas[figura]["ramo"] = ramo

def resultado_final():
    resultado = []
    for nome, dados in figuras_historicas.items():
        total = dados["impacto"] + dados["legado"]
        resultado.append((nome, dados["ramo"], total, dados["legado"], dados["impacto"]))

    resultado.sort(key=lambda dado: (-dado[2]))

    if resultado[0][2] == resultado[1][2]:
        figura1, figura2 = resultado[0][0], resultado[1][0]
        print(f"Temos um empate entre {figura1} e {figura2}, vamos usar os critérios de desempate para ver quem fica com o prêmio.")
        if ordem_relevancia[resultado[0][1]] > ordem_relevancia[resultado[1][1]]:
            figura1, figura2 = figura2, figura1
            vencedor = figura1
        print(f"Após utilizar os critérios de desempate, {vencedor} ficou com o prêmio.")
    else:
        figura1, figura2 = resultado[0][0], resultado[1][0]
    print(f"1º: {figura1} com {resultado[0][3]} pontos de legado, {resultado[0][4]} pontos de impacto e {resultado[0][2]} pontos totais")
    print(f"2º: {figura2} com {resultado[1][3]} pontos de legado, {resultado[1][4]} pontos de impacto e {resultado[1][2]} pontos totais")

processamento_bairros()
resultado_final()