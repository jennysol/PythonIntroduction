from datetime import date # importar data 
ano= int(input('Qual ano vai ser análisado?'))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
    