"""
Função help() and parametros opcionais 

def contador(i,f,p) = inicio, fim, passo
"""

def somar(a=0, b=0, c=0): #Parametros opcionais
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Jennifer Soliver
    """

    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,1)

# ESCOPO DE VARIÁVEIS

"""

def teste():
    global n
    n = 8
    print(f'Na função, n vale {n}') -> Variaval global
    print(f'Na função teste, x vale {x}) -> Variavel local

n = 2
print(f'No programa principal, n vale {n}')
teste()

se colocar global n o n pode mudar o valor

"""