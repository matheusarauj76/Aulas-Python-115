# Titulo: Dolar
# Autor: Matheus Araujo
# Data: 19/09/2024
# Descrição: Faça um algorítmo que um valor na moeda real a cotação da conversao real para dolar e apresente a quantidade do valor em dolar

#entrada
real = float(input("Insira o valor em reais"))
dolar = float(input("Insira o valor da cotação"))

#processamento
dolar = real * dolar

#saída
print("R$" + str(real) + " equivalem a $" + str(dolar))
print(f"R${real} equivalem a ${dolar}") #f significa format. Basta usar e colocar os campos nas chaves "{}", e o texto pode ser colocado normalmente entre aspas por toda a string