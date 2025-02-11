def calcular_taxa (total_recursos, populacao_piltover, populacao_zaun, situacao_zaun):
    if situacao_zaun == "desastre":
        taxa_distribuicao = 0.9
    elif situacao_zaun == "crise":
        taxa_distribuicao = 0.8
    elif situacao_zaun == "critica":
        taxa_distribuicao = 0.7
    elif situacao_zaun == "normal":
        taxa_distribuicao = 0.6
    elif situacao_zaun == "tranquilo":
        taxa_distribuicao = 0.5
    else:
        taxa_distribuicao = False
    return taxa_distribuicao

def distribui_recursos(taxa_distribuicao, total_recursos):
        recursos_zaun = total_recursos * taxa_distribuicao
        recursos_piltover = total_recursos-recursos_zaun
        return recursos_zaun, recursos_piltover
    
def mensagens(recursos_zaun, recursos_piltover):
    razao = recursos_zaun / recursos_piltover
    if razao >= 0.9:
        mensagem = ("Zaun receberá uma bolada!!!")
    elif razao >= 0.8:
        mensagem = ("Quase que Piltover ficava sem nada, pobrezinhos...")
    elif razao >= 0.7:
        mensagem = ("O negócio vai ficar bom para Zaun hein.")
    elif razao >= 0.6:
        mensagem = ("Parece que Zaun ainda precisa de ajuda.")
    elif razao >= 0.5:
        mensagem = ("As coisas estão meio apertadas para Zaun.")
    else:
        mensagem = ("A situação não está muito favorável para Zaun...")
    return mensagem

total_recursos = int(input())
populacao_piltover = int(input())
populacao_zaun = int(input())
situacao_zaun = input()

taxa_distribuicao = calcular_taxa(total_recursos, populacao_piltover, populacao_zaun, situacao_zaun)
if taxa_distribuicao:
    recursos_zaun, recursos_piltover = distribui_recursos(taxa_distribuicao, total_recursos)
else:
    soma_populacoes = populacao_piltover + populacao_zaun
    recursos_piltover = total_recursos * populacao_piltover / soma_populacoes
    recursos_zaun = total_recursos * populacao_zaun / soma_populacoes
print(f"Foi decidido que será {recursos_piltover:.1f} para Piltover e {recursos_zaun:.1f} para Zaun!")
mensagem = mensagens(recursos_zaun, recursos_piltover)
print(mensagem)