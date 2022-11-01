print("Digite o tipo de tabela  verdade que você quer consultar")

print("1 - p ^ q")
print("2 - p v q")
print("3 - p --> q")
print("4 - p - <--> q")

tipoTabela=int(input())

if(tipoTabela ==1):
    print('p  q  p^q')
    print( 'V V   V')
    print( 'V F   F')
    print( 'F V   F')
    print( 'F F   F')

if(tipoTabela==2):
    print('p   q  pVq')
    print( 'V  V   V')
    print( 'V  F   V')
    print( 'F  V   V')
    print( 'F  F   F')


#suficiente --> necessario
#  condicional só será falsa se a 
#  antecedente (lado esquerdo da seta) for verdadeiro e a consequente (lado direito) da seta for falso.
if(tipoTabela==3):
    print(' p  q  p-->q')
    print( 'V  V    V')
    print( 'V  F    F')
    print( 'F  V    V')
    print( 'F  F    V')


# As duas tem que ser iguais pra dar Verdadeiro
if(tipoTabela ==4):
    print(' p  q   p<-->q')
    print( 'V  V     V')
    print( 'V  F     F')
    print( 'F  V     F')
    print( 'F  F     V')