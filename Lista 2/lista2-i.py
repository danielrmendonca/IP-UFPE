altura_triangulo = int(input())
altura_total = 2*altura_triangulo-1
espaco = "⠀"

for i in range (1, altura_total + 1):
  if i == 1 or i == altura_total:
    espaco_lateral = espaco*(altura_triangulo-1)
    tamanho_espaco_lateral = altura_triangulo-1
    concatenacao = (espaco_lateral + "*" + espaco_lateral)
    print(concatenacao)
  elif i == altura_triangulo:
    asteriscos = (("*"+espaco)*(altura_triangulo-1))
    concatenacao = asteriscos+"*"
    print(concatenacao)
    tamanho_espaco_lateral = 0
  elif i < altura_triangulo:
    tamanho_espaco_lateral -= 1
    espaco_lateral = tamanho_espaco_lateral * espaco
    espaco_central = espaco*(2*(i-1)-1)
    concatenacao = espaco_lateral + "*" + espaco_central + "*" + espaco_lateral
    print(concatenacao)
  else:
    novo_i = altura_triangulo*2 - i
    tamanho_espaco_lateral += 1
    espaco_lateral = tamanho_espaco_lateral * espaco
    espaco_central = espaco*(2*(novo_i-1)-1)
    concatenacao = espaco_lateral + "*" + espaco_central + "*" + espaco_lateral
    print(concatenacao)