nome_do_jogador_1 = str(input())
quantidade_de_gols_1 = int(input())
quantidade_de_partidas_1 = int(input())
velocidade_maxima_1 = float(input())

pontuacao_final_1 = ((quantidade_de_gols_1 * 5) + (quantidade_de_partidas_1 * 2) +(velocidade_maxima_1 * 3))/10 + (len(nome_do_jogador_1) % 3)

nome_do_jogador_2 = str(input())
quantidade_de_gols_2 = int(input())
quantidade_de_partidas_2 = int(input())
velocidade_maxima_2 = float(input())

pontuacao_final_2 = ((quantidade_de_gols_2 * 5) + (quantidade_de_partidas_2 * 2) +(velocidade_maxima_2 * 3))/10 + (len(nome_do_jogador_2) % 3)

nome_do_jogador_3 = str(input())
quantidade_de_gols_3 = int(input())
quantidade_de_partidas_3 = int(input())
velocidade_maxima_3 = float(input())

pontuacao_final_3 = ((quantidade_de_gols_3 * 5) + (quantidade_de_partidas_3 * 2) +(velocidade_maxima_3 * 3))/10 + (len(nome_do_jogador_3) % 3)

if pontuacao_final_1 > pontuacao_final_2 and pontuacao_final_1 > pontuacao_final_3:
    primeiro = nome_do_jogador_1
    pontuacao_1 = pontuacao_final_1
    if pontuacao_final_2 > pontuacao_final_3:
        segundo = nome_do_jogador_2
        pontuacao_2 = pontuacao_final_2
        terceiro = nome_do_jogador_3
        pontuacao_3 = pontuacao_final_3
    else:
        segundo = nome_do_jogador_3
        pontuacao_2 = pontuacao_final_3
        terceiro = nome_do_jogador_2
        pontuacao_3 = pontuacao_final_2

elif pontuacao_final_2 > pontuacao_final_1 and pontuacao_final_2 > pontuacao_final_3:
    primeiro = nome_do_jogador_2
    pontuacao_1 = pontuacao_final_2
    if pontuacao_final_1 > pontuacao_final_3:
        segundo = nome_do_jogador_1
        pontuacao_2 = pontuacao_final_1
        terceiro = nome_do_jogador_3
        pontuacao_3 = pontuacao_final_3
    else:
        segundo = nome_do_jogador_3
        pontuacao_2 = pontuacao_final_3
        terceiro = nome_do_jogador_1
        pontuacao_3 = pontuacao_final_1

else:
    primeiro = nome_do_jogador_3
    pontuacao_1 = pontuacao_final_3
    if pontuacao_final_1 > pontuacao_final_2:
        segundo = nome_do_jogador_1
        pontuacao_2 = pontuacao_final_1
        terceiro = nome_do_jogador_2
        pontuacao_3 = pontuacao_final_2
    else:
        segundo = nome_do_jogador_2
        pontuacao_2 = pontuacao_final_2
        terceiro = nome_do_jogador_1
        pontuacao_3 = pontuacao_final_1

print(f'1 - {primeiro} obteve {pontuacao_1:.2f} pontos.')
print(f'2 - {segundo} obteve {pontuacao_2:.2f} pontos.')
print(f'3 - {terceiro} obteve {pontuacao_3:.2f} pontos.')
print(f'{primeiro} é o verdadeiro ganhador da Bola de Ouro com um total de {pontuacao_1:.2f} pontos.')
