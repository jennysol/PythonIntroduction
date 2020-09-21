#            Condições
# todo método carro.siga()
# 
#     if> se if carro.esquerdo():
# true &  elsefalse
# Somente o if para estrturas simples e if else para estruturas compostas 

#if tempo <=3:
#  print('carro novo')
#else: 
#  print('carro velho')
#print('--Fim---)

nome= str(input('Qual é o seu nome?'))
if nome == 'Jennifer':
    print('Que nome lindo você tem!')

else:
    print('Seu nome é tão normal, fofa!')

print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m  = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))

if m>= 6.0:
    print('Sua média foi boa! Fez sua obrigação')
else:
    print('Sua média foi ruim! Estuda mais criatura!')
