taxa_fixa_1 = float(input())
taxa_variavel_1 = float(input())
taxa_fixa_2 = float(input())
taxa_variavel_2 = float(input())

if taxa_fixa_1 == taxa_fixa_2 and taxa_variavel_1 == taxa_variavel_2:
    print('As duas empresas possuem o mesmo preço sempre!')
elif taxa_fixa_1 <= taxa_fixa_2 and taxa_variavel_1 <= taxa_variavel_2:
    empresa_mais_barata = 'Empresa 1'
    print(f'A {empresa_mais_barata} é sempre a melhor opção!')
elif taxa_fixa_2 <= taxa_fixa_1 and taxa_variavel_2 <= taxa_variavel_1:
    empresa_mais_barata = 'Empresa 2'
    print(f'A {empresa_mais_barata} é sempre a melhor opção!')
# tvk+tf = tv'k+tf' => tvk-tv'k = tf'-tf => k(tv-tv')=tf'-tf  => k=tf'-tf/tv-tv'
else:
    taxa_variavel_1 - taxa_variavel_2 != 0 and taxa_variavel_1 != taxa_variavel_2
    k = (taxa_fixa_2 - taxa_fixa_1)/(taxa_variavel_1 - taxa_variavel_2)
# é mais barato quem tem a menor taxa fixa porque a taxa fixa é o b da função
    if taxa_fixa_1 < taxa_fixa_2:
        empresa_x = 'Empresa 1'
        empresa_y = 'Empresa 2'
    else:
        empresa_x = 'Empresa 2'
        empresa_y = 'Empresa 1'
    print(f'{empresa_x} é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a {empresa_y} é mais barata para distâncias maiores que {k:.2f} km.')