#  Faça um programa que calcule a tabuada de um número digitado pelo usuário;

numero = int(input("Digite o número que deseja visualizar a tabuada"))
contador = 0

while contador <50:
    contador = contador + 1
    tabuada = (numero * contador)
    print(numero, "*", contador, "=",tabuada)
# print(numero, "* 1 = ", numero * 1)
# print(numero, "* 2 = ", numero * 2)
# print(numero, "* 3 = ", numero * 3)
# print(numero, "* 4 = ", numero * 4)
# print(numero, "* 5 = ", numero * 5)
# print(numero, "* 6 = ", numero * 6)
# print(numero, "* 7 = ", numero * 7)
# print(numero, "* 8 = ", numero * 8)
# print(numero, "* 9 = ", numero * 9)
# print(numero, "* 10 = ", numero * 10)
