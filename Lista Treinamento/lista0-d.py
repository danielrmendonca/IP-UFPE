diamantes_luiz = int(input())
diamantes_pedro = int(input())
diamantes_arthur = int(input())
horas = int(input())

max_luiz_pedro = (diamantes_luiz + diamantes_pedro + (abs(diamantes_luiz - diamantes_pedro))) /2
max_luiz_pedro_arthur = (max_luiz_pedro + diamantes_arthur + (abs(max_luiz_pedro - diamantes_arthur))) /2

max_diamantes = int(max_luiz_pedro_arthur * horas)

print(max_diamantes)