# Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
# salário, sabendo-se que este sofreu um aumento de 25%.

salario = float(input("Qual seu salário?"))
aumento = 0.25
novo_salario = salario * aumento + salario 
print("Parabéns, você recebeu um aumento de 25%")
print(f"Seu novo salário é de {novo_salario}")
