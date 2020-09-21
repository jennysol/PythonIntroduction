a= int(input('Primeiro número:'))
b= int(input('Segundo número:'))
c= int(input('Terceiro número:'))
#Verificando o menor
menor = a
if b<a and b<c:
   menor = b
if c<a and c<b:
    menor = c
#Verificando o maior
maior= a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior= c

print('O menor número é {}'.format(menor))    
print('O maior número é {}'.format(maior))    