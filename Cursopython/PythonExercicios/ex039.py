from datetime import date
atual = date.today().year
nasc = int(input('Ano em que nasceu:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos no ano atual.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar esse ano')
elif idade <18 :
    print('Você ainda não precisa se alistar')
elif idade > 18:
    print('Você ja devia ter se alistado, coisa!')
