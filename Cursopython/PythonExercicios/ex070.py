total = totmil = menor = cont = 0
while True:
    nome = str(input('Nome do produto:'))
    preço = int(input('Preço do produto:'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper() [0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi {total}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto de menor preço custa R${menor}')