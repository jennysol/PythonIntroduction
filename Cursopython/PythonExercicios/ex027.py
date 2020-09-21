n= str(input('Digite teu nome completo:')).strip()
nome= n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu últmo nome é{}'.format(nome[len(nome)-1]))