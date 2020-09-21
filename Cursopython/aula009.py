# Manipulando cadeias de texto 
             # [C][u][r][s][o][][e][m][][V][í][d][e][o][][P][y][t][h][o][n]
             # 0  1  2  3  4   5 6  7  8 9 10 11 12 13 14 15 16 17 18 19 20
             # [             ]  [    ] [              ]  [                ]
       # split              0          1           2                   3            
#             Fatiamento de string 
# No fatiamento o último valor sempre é ignorado pelo python
# frase[9] , [9:13] > sempre um a menos
# frase[:5] > quando omtir o inicio ele começa do zero
# frase[0::3]> ir até o fim ignorando de três em três

#                    Análise
#len(frase) = ao total de carcateris que a frase tiver +1 =21
#farse.count('o',0,13) > Quantas vezes aparece a letra 'o' minuscula = 3
#frase.find('deo')> Quantas vezes ele encontrou 'deo', Quando 'deo' começou = 11
#'Curso' in frase 

#                    Transformação
#frase.replace('Python' , 'Android) > substituir 
#frase.uppear() > Vai transformar em maíusculas 
#frase.lower() > Mantem o que é maísuculas e substitui por minusculas 
#frase.capitalize() > Deixar só a inicial da frase maíscula 
#frase.title() > Análisa os títulos e coloca as iniciais em maíusculas 
#frase.strip() > Remover os espaços inúteis da sua frase
#frase.split() > Vai dividir os espaçamentos em conteiner de palavras 
#len(frase) > Comprimento de frase = 21

#                     Junção
#'-' .join(frase) > Juntar frase
# https://pythonhoje.wordpress.com/2018/01/23/python-3-manipulando-cadeia-de-caracteres/

frase= 'Curso em Vídeo Python'
frase= frase.replace('Python', 'Android')
print(frase)
dividido = frase.split()
print(dividido)