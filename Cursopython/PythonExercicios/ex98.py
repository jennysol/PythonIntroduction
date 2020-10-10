'''
Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
 através da função criada: 
  a) de 1 até 10, de 1 em 1                                                                      
 b) de 10 até 0, de 2 em 2 
 c) uma contagem personalizada
'''
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(1)
            cont += p
        print('Fim!')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')



# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem !')

ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)