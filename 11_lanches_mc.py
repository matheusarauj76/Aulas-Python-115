# Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do 
# mesmo pelo usuário, de acordo com a tabela abaixo:
# Nr. Lanche
# 1 Big Mac
# 2 Quarteirão
# 3 McChicken
# 4 Cheddar McMelt
# 5 McMax

#entrada
lanche = int(input("Digite o cód do lanche:"))
#processamento e saída
if lanche == 1:
    print("Big Mac")
elif lanche == 2:
    print("Quarteirao")
elif lanche == 3:
    print("McChicken")
elif lanche == 4:
    print("Cheddar McMelt")
elif lanche == 5:
    print("McMax")
else:
    print("O código do lanche não existe!")
