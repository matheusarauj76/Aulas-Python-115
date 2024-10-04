#Titulo: Ocupação funcionário
#Autor: Matheus Araujo
#Data: 01/10/2024
#Descrição: Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão, de acordo com a tabela abaixo;
# Código de Profissão Ocupação
# 1 Matemático
# 2 Analista de Sistemas
# 3 Físico
# 4 Arquiteto
# 5 Piloto de Aeronaves

# entrada

codigo_profissao = input(int("Insira o código de profissão:"))

# processamento e saída

if codigo_profissao == 1:
    print("Matemático")
if codigo_profissao == 2:
    print("Analista de Sistemas")
if codigo_profissao == 3:
    print("Físico")
if codigo_profissao == 4:
    print("Arquiteto")
if codigo_profissao == 5:
    print("Piloto de Aeronaves")
else:
    print("Código de profissão não encontrada, tente novamente!")