dias = int(input())
casas = int(input())

horas = dias * 3
minutos = horas * 60

dias_minecraft = minutos / 20
ticks = dias_minecraft * 24000
ticks_casa = int((ticks / casas) / 2) #apenas no ciclo diurno

print(ticks_casa)