""" 
CURSO PYTHON TUPLAS > Variavéis compostas !

Método len > Referência a comprimento
variável simples > só aceita um comando

AS TUPLAS SÃO IMUTÁVEIS

()> tupla {}> lista []> dicionário
- Parte prática 
"""
lanche = ('batata', 'suco' ,'pizza' , 'pudim') #usar com ou sem parenteses
#print(lanche [2])
#print(lanche[1:3]) # Aqui ele seleciona de ponto de partida até ponto de chegada = suco, pizza > o último elemento sempre é 
#print(len(lanche))


for cont in range(0, len(lanche)):
    print(lanche[cont])
   #print(f'Eu vou comer {comida}')

for comida in lanche:
    print(f'Eu voucomer{comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4, 7)
b = (3, 5, 8, 9)
c = b + a
print(c.count(5))