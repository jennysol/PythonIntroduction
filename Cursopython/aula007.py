# Operações matemáticas

# + Adição
# - Subtração
# * Multiplicação 
# / Divisão
# ** Potência 
# // Divisão
# % Resto da divisão

# Ordem de proedencia

#1 - ()
#2 - **
#3 - * / // % 
#4 - + - 

# ( 5+3*2)== 11
# ( 3*5+4 **2)== 31 
#  3* (5 + 4) ** 2 == 243

n1= int(input('Outro valor:'))
n2= int (input('Outro valor:'))
s= n1+ n2
m= n1 * n2
d= n1 / n2 
di= n1 // n2
p= n1 ** n2
print( 'A soma é {} ,\n o produto é {} e a divisão é {}'.format(s, m,d))
print('Divisão inteira {} e potência {}' .format(di, p))


