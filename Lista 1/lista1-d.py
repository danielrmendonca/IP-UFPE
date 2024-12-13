voto1 = input()
pais1 = input()
voto2 = input()
pais2 = input()

qtd_votos_vini = 0
qtd_votos_rodri = 0

if pais1 == 'Espanha' and voto1 == 'rodri':
    votacao1 = 'não registrado'
elif pais1 == 'Brasil' and voto1 == 'vinijr':
    votacao1 = 'não registrado'
else: votacao1 = 'registrado'

if votacao1 == 'registrado':
     print('Voto registrado!') 
else: print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')

if voto1 == 'vinijr' and votacao1 == 'registrado':
        qtd_votos_vini += 1
elif voto1 == 'rodri' and votacao1 == 'registrado':
        qtd_votos_rodri += 1

if pais2 == 'Espanha' and voto2 == 'rodri':
    votacao2 = 'não registrado'
elif pais2 == 'Brasil' and voto2 == 'vinijr':
    votacao2 = 'não registrado'
else: votacao2 = 'registrado'

if votacao2 == 'registrado':
     print('Voto registrado!')
else: print('Voto inválido! Não é permitido votar em jogadores do mesmo país.')

if voto2 == 'vinijr' and votacao2 == 'registrado':
    qtd_votos_vini += 1
elif voto2 == 'rodri' and votacao2 == 'registrado':
    qtd_votos_rodri += 1

print(f'Votos válidos para rodri: {qtd_votos_rodri}')
print(f'Votos válidos para vinijr: {qtd_votos_vini}')