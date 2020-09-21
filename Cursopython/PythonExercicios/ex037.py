num = int(input('Digite um número Inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))
elif opção == 1:
    print('{} convertido para Binário é igual {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print( 'Opção inválida. Tente Novamente!')
    