# Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que 
# pertence, de acordo com a tabela abaixo;
# Faixa etária Classificação
# <12 Criança
# 13~17 Adolescente
# 18^59 Adulto
# >60 Especialista

#entrada
idade = int(input("Digite a idade:"))

#processamento e saída
if idade <=12:
    print("Criança")
elif idade <=17:
    print("Adolescente")
elif idade <=59:
    print("Adulto")
else:
    print("Especialista")