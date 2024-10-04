#Titulo: Dólar
#Autor: Julio Miranda
#Data: 19/09/2024
#Descrição: Faça um algoritmo que um valor na moeda real (R$),
#           a cotação da conversão REAL para DÓLAR, e apresente
#           a quantidade desse valor em dólar ($)
#           ------------------------------------------
#           Exemplo de execução
#           Insira o valor em real: 5000
#           Insira cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#           ----------------------------------------

#entrada de dados
moeda_real = input("Insira o valor em reais:")
cotacao_dia = input("Insira o valor da cotação:")
#processamento de dados
moeda_real = int(moeda_real)
cotacao_dia = int(cotacao_dia)
moeda_dolar = moeda_real / cotacao_dia
#saida de dados
print(f'R$ {moeda_real} equivalem $ {moeda_dolar}') #format
print('R$ ' + str(moeda_real) + ' equivalem $ ' + str(moeda_dolar))