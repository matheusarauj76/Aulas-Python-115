# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Alo mundo")

# # Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# numero = input("Digite um número")
# print("O número informado foi " + str(numero))

# # Faça um Programa que peça dois números e imprima a soma.
# numero1 = int(input("Digite o primeiro número"))
# numero2 = int(input("Digite o segundo número"))
# soma = numero1 + numero2
# print(soma)

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# nota1 = 2
# nota2 = 8
# nota3 = 10
# nota4 = 10
# soma = nota1 + nota2 + nota3 + nota4
# media = soma/4
# print(media)

# Faça um Programa que converta metros para centímetros.
# metros = int(input("quantos metros voce quer converter?"))
# centimetros = metros * 100
# print(centimetros)

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# r = int(input("Qual o raio do circulo?"))
# pi = 3.14
# area = r * r * pi
# print(area)

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# lado_quadrado = int(input("Qual o valor do lado do quadrado?"))
# area_quadrado = lado_quadrado * 4
# dobro_area = area_quadrado * area_quadrado
# print(f"A área do quadrado em dobro é de {dobro_area}")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# salario_mensal = float(input("Qual sue salário atual?"))
# salario_hora = salario_mensal / 160
# salario_dia = salario_hora * 8
# salario_semana = salario_dia * 5
# print(f"Você ganha {salario_hora} por hora de trabalho, {salario_dia} por dia e {salario_semana} por semana trabalhada.")

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# temperatura_f = float(input("Qual a temperatura em graus Fahrenheit?"))
# temperatura_c = (temperatura_f - 32) / 1.8  
# print(f"Você informou a temperatura {temperatura_f}°F. Essa temperatura em Celsius é de {temperatura_c}°C)")
# °C = (°F − 32) ÷ 1, 8

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# temperatura_c = float(input("Qual a temperatura em graus Celsius?"))
# temperatura_f = temperatura_c * 1.8 + 32 
# print(f"Você informou a temperatura {temperatura_c}°C. Essa temperatura em Fahrenheit é de {temperatura_f}°F)")

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
# numero1_int = int(input("Digite um número inteiro"))
# numero2_int = int(input("Digite um segundo número inteiro"))
# numero3_real = float(input("Digite um terceiro número real"))
# print((numero1_int * numero1_int) * (numero2_int / 2))
# print((numero1_int + numero1_int + numero1_int) + numero3_real)
# print(numero3_real * numero3_real * numero3_real)

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# h = float(input("Digite sua altura"))
# peso_ideal = (h * 72.7) - 58
# print(f"Seu peso ideal é de {peso_ideal}")

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# h = float(input("Digite sua altura"))
# peso_ideal_h = (h * 72.7) - 58
# peso_ideal_m = (h * 62.1) - 44.7
# print(f"Se você for homem, seu peso ideal é de {peso_ideal_h}, se for mulher é de {peso_ideal_m}")
# sexo = input("Você é homem ou mulher?").lower()
# if  sexo == "homem":
#     print(f"Você é homem, seu peso ideal é de {peso_ideal_h}")
# elif sexo == "mulher":
#     print(f"Você é mulher, seu peso ideal é de {peso_ideal_m}")

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa 
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
# deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# peso_peixes = float(input("Quantos kg de peixes você pescou?"))
# peso_regulamento = 50
# peso_excedido = peso_peixes - peso_regulamento
# multa = round(peso_excedido * 4, 2)
# multa_formatada = f"{multa:.2f}"

# if peso_peixes > 50:
#     print(f"Você informou que pescou um total de {peso_peixes}kg. Como o regulamento prevê o limite de até {peso_regulamento}kg, você ultrapassou {peso_excedido}kg, gerando uma multa de R$ {multa_formatada}.")
# else:
#     print(f"Você informou que pescou um total de {peso_peixes}kg, não excedeu o regulamento de {peso_regulamento}kg, portanto não pagará nenhuma multa.")
                    
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# salario_hora = float(input("Quanto você ganha por hora?"))
# horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? (Um clt comum que trabalha 40 horas semanais trabalha em média 200 horas mensais)."))
# salario_bruto_mes = salario_hora * horas_trabalhadas
# salario_bruto = f"{salario_bruto_mes:.2f}"
# inss_mes = (salario_bruto_mes / 100 * 8)
# inss = f"{inss_mes:.2f}"
# sindicato_mes = salario_bruto_mes / 100 * 5
# sindicato = f"{sindicato_mes:.2f}"
# ir_mes = salario_bruto_mes / 100 * 11
# ir = f"{ir_mes:.2f}"
# descontos_mes = inss_mes + ir_mes + sindicato_mes
# descontos = f"{descontos_mes:.2f}"
# salario_liquido_mes = salario_bruto_mes - descontos_mes
# salario_liquido = f"{salario_liquido_mes:.2f}"
# print(f"Seu salário bruto no mês é de R$ {salario_bruto}. Porém, você recebe vários descontos, como INSS: R$ {inss}, IR: R$ {ir}, desconto sindical: R$ {sindicato}. Com todos esses descontos (que somam R$ {descontos}, seu salário líquido é de {salario_liquido})")

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
# 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Qual o tamanho (em metros quadrados) da área a ser pintada?"))
l_tinta = 18
v_tinta = 80
l_quadrado = 1 / 3
l_tinta_area_pintada = l_tinta * area
v_tinta_area_pintada = v_tinta * area
print(f"Com uma área de {area} metros quadrados, você precisa de {l_tinta_area_pintada} litros de tinta, e gastará o total de R${v_tinta_area_pintada}.")


# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
