num = 0 
soma = 0
quant = 0
while True :
    num = int(input('Digite um número interio?: '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'A quantidade adiconada foi {quant} e a soma é igual {soma}')