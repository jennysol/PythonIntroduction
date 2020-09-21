# CONDIÇÕES ANINHADAS 
# IF 
# ELIF ( Opcional )
# ELSE ( Opcional)

nome= str(input('Qual é o seu nome :'))
if nome == 'Jennifer':
    print('Que nome LIndo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil, né Anjo')
elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome feminino! ')
else: 
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))
