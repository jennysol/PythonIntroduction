# append adicona elementos no final da lista
# len demonsta o tamanho da lista
# .sort demostra os valores de forma crescente
# .sort(reverse=True) demonstra os valores de froma decrescente.
valores = []

while True: 
    valores.append(int(input("Digite um valor:")))
    resp = str(input("Quer continuar [S/N]"))
    if resp in 'Nn':
        break

print("-=" *30)

print(f'Você digitou {len(valores)} elementos.')

valores.sort(reverse=True)
print(f'Os valores de forma decrescente {valores}')

if 5 in valores: 
    print('O valor 5 foi encontrado na lista.')
else: 
    print('O valor 5 não foi encontrado na lista.')
