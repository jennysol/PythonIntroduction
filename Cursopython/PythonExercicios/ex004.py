a = input('digite algo:')
print('o tipo primitivo desse valor é ' , type(a))
print('Só teme espaços?', a.isspace()) #para identificar se é só espaço / true or false
print('É um número?', a.isnumeric()) # para identificar se são números
print('É alfabetico?', a.isalpha()) # retorna true se todos os carcateres forem letras
print('É alfanumérico?', a.isalnum()) # retornar tru se todos os caracteres forem alfanuméricos , de A a Z
print('Está em maiúsculas?', a.isupper()) # retorna true para letras maiúsculas
print('Está em minúsculas', a.islower()) # retorna true letras minúsculas
