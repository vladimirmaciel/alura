idades = [15, 87, 32, 65, 56, 32, 49, 37]
# for i in range(len(idades)):
#     print(i, idades[i])

enumerate(idades)  # lazy
# print(list(range(len(idades))))  # forçei a geração dos valores

# print(list(enumerate(idades)))

for valor in enumerate(idades):  # incrementa na medida que for necessário
    print(valor)

# incrementa na medida que for necessário
for indice, idade in enumerate(idades):  # unpacking da nossa tupla
    print(indice, ":", idade)

usuarios = [("Guilherme", 37, 1981), ("João", 23, 1990), ("Maria", 37, 1986)]

for nome, idade, nascimento in usuarios:  # ja descempacotando
    print(nome)

for nome, _, _ in usuarios:  # ja descempacotando _ ignora as outras variaveis
    print(nome)
