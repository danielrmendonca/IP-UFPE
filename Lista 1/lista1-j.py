projecao_desempenho = str(input())
projecao_pgols = int(input())
desempenho_final = str(input())
print('Está aberta a revisão da premiação!')

pontuacao = 0
#rodri pontuação 1170 importante
desempenho_final_rodri = 350

if projecao_desempenho == 'Decepção':
    pontuacao_d = 100
elif projecao_desempenho == 'Oscilação':
    pontuacao_d = 200
elif projecao_desempenho == 'Importante':
    pontuacao_d = 300
else: pontuacao_d = 400
pontuacao += pontuacao_d
if pontuacao_d == 100:
    print('Parece que não estão colocando muitas expectativas para a temporada do nosso Vini Jr., não... Sempre subestimado!')
elif pontuacao_d == 200:
    print('Os jornalistas acreditam que Vini Jr. terá atuações irregulares nesta temporada, mas quem sabe ele não supera as projeções?')
elif pontuacao_d == 300:
    print('Em um elenco tão forte como o do Real Madrid, é normal as atenções serem divididas mesmo. O que importa é que ele não vai se esconder!')
else: print('Vini Jr. será o craque do Real Madrid na temporada de 2023/2024! Será que ele consegue a tão sonhada Bola de Ouro?')

pontuacao_pg = (projecao_pgols * 2) + (pontuacao_d / 2)
pontuacao += pontuacao_pg

if desempenho_final == 'Decepção':
    pontuacao_df = 150
elif desempenho_final == 'Oscilação':
    pontuacao_df = 250
elif desempenho_final == 'Importante':
    pontuacao_df = 350
else: pontuacao_df = 500
pontuacao += pontuacao_df
if pontuacao_df == 150:
    print('Vini Jr. decepcionou os torcedores em 2024, não era o ano dele.')
elif pontuacao_df == 250:
    print('A temporada não foi das melhores, mas Vini Jr. conseguiu mostrar, em alguns momentos, que ele de fato é craque.')
elif pontuacao_df == 350:
    print('Vini Jr. mostrou que é crucial para o elenco do Real Madrid e da Seleção.')
else: print('Ele é demais! Herói do título da Champions, ele conseguiu mostrar ao mundo que é uma estrela do futebol!')

if pontuacao_df > pontuacao_d and desempenho_final != projecao_desempenho:
    pontuacao += 300
    print('Ele sempre aparece em momentos importantes! Nunca duvidem do Malvadeza, ele é muito craque!')
elif desempenho_final == projecao_desempenho:
    pontuacao += 100
    print('A mídia estava certa! Vini Jr. se manteve dentro das projeções dos jornalistas, mas será que é suficiente para vencer o Rodri?')
else: print('É, parece que Vini Jr. foi mal esse ano, o sonho está cada vez mais distante.')

if 37 > projecao_pgols:
    print('Vini Jr. foi muito decisivo para sua equipe este ano, superando sua previsão de participações em gols!')
else: print('É, Vini Jr. não conseguiu provar que estavam errados, mas ainda assim ele segue vivo para a premiação.')

if pontuacao > 1170:
    print(f'O mundo estava certo! Com {int(pontuacao)} pontos, Vini Malvadeza é o verdadeiro melhor do mundo! Chega dessa injustiça!')
elif 1170 > pontuacao:
    print('Infelizmente, teremos que nos contentar com o Rodri sendo o melhor do mundo mesmo.')
else:
    print('Empate! Vamos ao critério de desempate.')
    if pontuacao_df > desempenho_final_rodri:
        print('Foi uma premiação apertada, mas a justiça foi feita! Vini Jr. é, sim, o melhor do mundo.')
    else: print('Bom, é isso. Ainda tivemos esperanças, mas o Rodri é, mesmo, o Bola de Ouro.')