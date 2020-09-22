# Listas Compostas

# pessoas.append(dados[:]) Buscar uma estrutura, copiar e juntar
# pessoas = [['Pedro', 25], ['Maria',19]] > Listas compostas

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

galera = list()
dado = list() # Estrutura auxiliar para transmitir dados
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear() # parametro para limpar todos os itens da lista.

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
