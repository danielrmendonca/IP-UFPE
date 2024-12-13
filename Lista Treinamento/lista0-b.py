x_steve = int(input())
z_steve = int(input())

distancia_h = ((34-x_steve)**2 +(220-z_steve)**2)**(1/2)
distancia_k = ((0-x_steve)**2 +(0-z_steve)**2)**(1/2)
distancia_s = ((140-x_steve)**2 +(456-z_steve)**2)**(1/2)

print(f'Distancia para Hogsmeade: {distancia_h:.2f}')
print(f'Distancia para Kakariko: {distancia_k:.2f}')
print(f'Distancia para Solitude: {distancia_s:.2f}')