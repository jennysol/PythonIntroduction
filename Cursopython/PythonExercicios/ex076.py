listagem = ('lápis', 1.45, 'borracha', 2 , 'apontador' , 2.35, 'caneta',  3.40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=" ")
    else:
        print(f'R${listagem[pos]:<7.2f}')
