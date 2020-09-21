dis= float(input('Qual a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {} km.'.format(dis))
if dis <= 200:
   preço= dis * 0.50
else:
   preço = dis * 0.45
print('Sua viagem custará {:.2f}'.format(preço))   
