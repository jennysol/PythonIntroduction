print('-=-' *20)
print('Analisador de triangulos')
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro segmento:'))
if r1< r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem fromar um triangulo')
else:
    print('Os segmentos acima não podem formar um triangulo')