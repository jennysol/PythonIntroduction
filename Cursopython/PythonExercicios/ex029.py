velocidade= float(input('Qual a velocidade do seu carro?'))
if velocidade > 80:
    print('Multado! Você está muito rápido!')
    multa= (velocidade -80) *7
    print('Vocẽ deve pagar uma multa de R${:.2f}!'.format(multa))

print('Tenha uma boa viagem !')

