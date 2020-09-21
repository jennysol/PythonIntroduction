from random import randint
v = 0
while True:
    jogador = int(input('Digite um Valor :'))
    computador = randint (0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par or Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0 :
            print('Você Venceu!!')
            v += 1
        else:
            print('Você perdeu , me sorry bb ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu !!')
            v += 1
        else: 
            print('Você Perdeu , Criança')
            break
    print( 'Vamos jogar de novo , besta ! ')
print(f'Game Over! Você venceu {v} vezes.')
