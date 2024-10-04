# Faça um programa que receba 3 valores e verifique se eles podem representar os 
# lados em um triângulo;
# Nome Característica
# Equilátero 3 lados iguais
# Isósceles 2 lados iguais
# Escaleno 3 lados diferente
# Lembre-se que para formar um triângulo, nenhum dos lados pode ser igual a zero e 
# cada um dos lados precisa ser menor que a soma dos outros dois

#entrada
lado_1 = int(input("Digite o primeiro valor:"))
lado_2 = int(input("Digite o segundo valor:"))
lado_3 = int(input("Digite o terceiro valor:"))

#processamento
if lado_1 == 0 or lado_2 == 0 or lado_3 ==0:
    print("Você digitou um valor 0 e não pode representar os lados do triângulo.")
elif lado_1 > lado_2 + lado_3 or lado_2 > lado_1 + lado_3 or lado_3 > lado_1 + lado_2:
    print("Um dos lados do triângulo é maior do que a soma dos outros dois lados, impossível descobrir o tipo!")
elif lado_1 == lado_2 and lado_2 == lado_3:
    print("Esse triângulo é Equilatéro, pois possui os três lados iguais.")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("Esse triãngulo é Isósceles, pois possui 2 lados iguais.")
elif lado_1 != lado_2 and lado_2 != lado_3:
    print("Esse triângulo é Escaleno, pois possui os 3 lados diferentes.")


# saída
