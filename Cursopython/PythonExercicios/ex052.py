núm= int(input('Digite um número:'))
tot = 0
for c in range (1, núm + 1):
    if núm % c == 0:
        print(end= '')
        tot += 1
    else:
        print(end= '')
    print('{}'.format(c), end='')
print('O número {} foi divísivel {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('Por isso ele não é primo!')