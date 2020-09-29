"""
Adicionar Indices alfabéticos > Dicionários {}

# """
#  dados = dict()
#  dados = { 'nome': 'Pedro', 'idade': 25 } # Nomeando
#  dados['sexo'] = 'M' # Adicioando dados 
#  del dados['idade'] # deletando dados 
#  print(dados['nome']) # Mostrando

#print(dados.value())
#print(dados.keys())
#print(dados.items())

# for k,v in filme.items():
#     print(f'O {k} é {v}')

# pessoas = {'nome':'Jennifer', 'sexo':'F', 'idade': 18} 
# del pessoas['sexo'] # deletando
# pessoas['nome'] = 'Matheus' # Modificando
# pessoas ['peso'] = 45.0 # adicionando
# print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# print()
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# Criando um dicionário dentro de uma lista

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativva:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
    
