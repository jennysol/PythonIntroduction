qd= int(input( 'Quantos dias foi usado?'))
qk= float(input('Quantos km rodados?'))
pago= (qd*60) + (qk * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))