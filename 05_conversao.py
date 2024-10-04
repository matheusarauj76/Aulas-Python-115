# Faça um programa que recebe um número em Pés, faça as conversões a seguir e mostre os resultados:
#   Polegadas;
#   Milhas;
#   Jardas;
# Sabe–se que:
# 1 Pé = 12 polegadas;
# 1 Jarda = 3 Pés;
# 1 Milha = 1.760 Jarda;

#entrada
pes = int(input("Qual o número em pés?"))

#processamento
polegada = pes * 12
jarda = pes / 3
milha = jarda / 1760

print(f"Se seu pé é {pes}, então:")
print(f"A polegada é de {polegada};")
print(f"A jarda é de {jarda};")
print(f"A milha é de {milha}.")