valor= float(input('Qual o valor da casa? '))
salario= float(input('Qual o valor do seu salário?'))
anos = int(input('Em quantos anos você deseja pagar a casa ?'))
meses= anos *12
print(' Computando Valor da prestação mensal...')
prestação = valor/meses 
if prestação < (salario*30/100):
    print('Parábens, você foi aprovado!')
else:
    print('Sinto muito, você não corresponde aos critérios da empresa.')