sexo = str(input('Escolha o seu sexo ? [F/M]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input( 'Não definido! Por favor digite seu sexo:')).strip().upper()[0]
print( 'Definido com sucesso!')