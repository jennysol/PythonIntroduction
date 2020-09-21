somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print('-------- {} Pessoa ------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade 
    if p == 1 and sexo in 'Mm':
         maioridadehomem = idade
         nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade 
        nomevelho = nome 

médiaidade = somaidade / 4 
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print(' O home mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho)