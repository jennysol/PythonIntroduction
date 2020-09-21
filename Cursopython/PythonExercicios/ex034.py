salário= float(input('Digite seu salário:'))
if salário <= 1000:
    novo= salário + (salário *15 / 100 )
else:
    novo = salário + ( salário *10 /100 ) 
print('Seu salário será {}'.format(novo))
