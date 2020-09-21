altura = float(input('Qual é sua altura? (m)'))
peso= float(input('Qual é o teu peso em (kg)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5 :
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print ('Paranéns, você está na faixa de peso normal!')
elif 25 <= imc < 30:
    print('Vocẽ está em Sobrepeso')
elif 30 <= imc < 40:
     print('Você está em obsidade !')
elif imc >= 40:
    print ('Vôce está em obsidade móbida, cuidado!')