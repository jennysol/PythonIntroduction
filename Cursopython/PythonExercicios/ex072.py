cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    núm = int(input('Digite um número entre 0 e 10:'))
    if 0 <= núm <= 10:
        break
    print('Tente novamente.', end=" ")
print(f'Você digitou o número {cont[núm]}')






