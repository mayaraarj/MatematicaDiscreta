#Fazer tabela verdade dinâmica em python! (P V Q dá verdadeiro, o resto dá falso)

valorProposicao1 = input("Digite o valor da primeira proposição - V ou F").upper()
print(" ")
valorProposicao2 = input("Digite o valor da segunda proposição - V ou F").upper()

if (valorProposicao1 =="V" and valorProposicao2 == "V" ):
    print("Verdadeiro")
else:
    print("Falso")