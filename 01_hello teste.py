#modo script

nota1 = input("Qual a sua nota 1")
nota2 = input("Qual a sua nota 2")
nota3 = input("Qual a sua nota 3?")
nota4 = input("Qual a sua nota 4?")
nota5 = input("Qual a sua nota 5?")
soma = int(nota1) + int(nota2) + int(nota3) + int(nota4) + int(nota5)
media = int(soma) / 5



print("A primeira nota é "+ str(nota1))
print("A segunda nota é "+ str(nota2))
print("A terceira nota é " + str(nota3))
print("A quarta nota é " + str(nota4))
print("A quinta nota é " +str(nota5))
print("O total das notas foi de " + str(soma))
print("A média foi de " + str(media))

if media >=5:
    print("Parabéns, você foi aprovado :)") 
else:
    print("Tente novamente, você foi reprovado :(")
