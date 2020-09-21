n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção = int(input('>>>>Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a  {}'.format(n1, n2, soma))
    elif opção == 2:
        Multiplicação = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, Multiplicação))
    elif opção == 3:
        if n1> n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior ))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo Valor :'))
    elif opção == 5:
        print('Finalizando...')
    else: 
        print('Essa opção é invalida!')
print('Fim do Programa! Volte Sempre!')
