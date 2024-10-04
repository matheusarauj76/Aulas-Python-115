'''
Titulo: Estudo "if" usando o calculo da média
Autor: Julio Miranda
Data: 26/09/2024
Descrição: Algoritmo que calcula a média e apresenta o status de aprovado,
           reprovado ou recuperação.
'''
# ctrl + shift + alt + (cima/baixo/direita/esquerda)
#entrada de dados
nota_1 = int(input('Digite a nota 1 :'))
nota_2 = int(input('Digite a nota 2 :'))
nota_3 = int(input('Digite a nota 3 :'))
nota_4 = int(input('Digite a nota 4 :'))
#processamento de dados
media_aluno = (nota_1 + nota_2 + nota_3 + nota_4)/4

if media_aluno >= 60:
    print('Aluno aprovado')
if media_aluno < 40:
    print('Aluno reprovado')
if media_aluno >= 40 and media_aluno < 60:
    print('Aluno em recuperação')
#saida de dados
print(media_aluno)