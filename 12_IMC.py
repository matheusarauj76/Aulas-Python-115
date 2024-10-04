# Escreva um algoritmo que a partir da massa e da altura informados pelo usuário, 
# calcule e apresente seu IMC e sua classificação conforme a tabela abaixo:
# IMC Classificação
# < 18 Magreza
# 18 ~ 24,9 Saudável
# 25 ~ 29,9 Sobrepeso
# >= 30 Obesidade

#entrada
peso = float(input("Qual seu peso?(Em kg)"))
altura = float(input("Qual sua altura? (Em metros)"))

# processamento
imc = peso / (altura * altura)

# saída
print(imc)
if imc <18:
    print("Seu IMC é menor que 18, considerado Magreza.")
elif imc <24.9:
    print("Seu IMC está entre 18 e 24,9, considerado Saudável!")
elif imc <29.9:
    print("Seu IMC esta entre 25 e 29,9, considerado Sobrepeso.")
elif imc >=30:
    print("Seu IMC está maior que 30, considerado Obesidade.")