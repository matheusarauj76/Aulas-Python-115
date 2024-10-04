# Escreva um programa que leia a velocidade máxima permitida em uma avenida e 
# velocidade com que o motorista estava dirigindo nela e calcule a multa que uma 
# pessoa vai receber;
# Siga a tabela de multas
# Velocidade Ultrapassada Valor da Multa
# Até 10 km/h R$ 50,00
# 11 a 30 km/h R$ 100,00
# Mais 31 km/h R$ 200,00
# Exemplo: 
# Limite: 50 km/h
# Velocidade: 59 km/h
# Multa: R$ 50,00

# entrada
velocidade_via = int(input("Digite a velocidade da via:"))
velocidade_considerada = int(input("Digite a velocidade considerada:"))

# processamento e saída
if velocidade_considerada - velocidade_via == 0:
    print("Você estava no limite da via, parabéns!")
elif velocidade_considerada - velocidade_via <=10:
    print(f"Você ultrapassou até 10km/h do limite estabelecido de {velocidade_via}km/h, sua multa é de R$ 50,00")
elif velocidade_considerada - velocidade_via <=30:
    print(f"Você ultrapassou até 30km/h do limite estabelecido de {velocidade_via}km/h, sua multa é de R$ 100,00")
elif velocidade_considerada - velocidade_via >30:
    print(f"Você ultrapassou mais que 30km/h do limite estabelecido de {velocidade_via}km/h, sua multa é de R$ 200,00")
