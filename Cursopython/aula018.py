# Listas Compostas

# pessoas.append(dados[:]) Buscar uma estrutura, copiar e juntar
# pessoas = [['Pedro', 25], ['Maria',19]] > Listas compostas

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)