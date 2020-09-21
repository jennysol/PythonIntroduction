num = (int(input('digite um número: ')),
        int(input('digite outro número: ')),
        int(input('digite mais um número: ')),
        int(input('digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu  {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)} posição')
else: 
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=' ')