tot18 = totH =  totM20 = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
         totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas maiores que 18 anos é igual a {tot18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'Ao total temos {totM20} mulheres com menos de 20 anos cadastradas')