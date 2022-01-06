# Dicionário

aparicoes = {"Guilherme": 1, "cachorro": 2, "nome": 2, "vindo": 1}
verifica = aparicoes.get("nome", 0)
print(verifica)
print(aparicoes.get("xpo", 0))  #  se xpo não estiver no dicionario devolve zero
print(aparicoes.get("cachorro", 0))  #  como existe cahorro ele devolve a posição 2

print(type(aparicoes))
print(aparicoes)
# print(aparicoes["zpo"])

nome = dict(Vladimir=1, Amanda=2, Davi=3)  # outra forma de declara um dicionariao
print(nome)

nome["luke"] = 4
nome["Mel"] = 5
del nome["Mel"]
print("Vladimir" in nome)  # procurar nas chaver e não nos valores

for n in nome.values():
    print(n)

# utilizamos o keys é para pegar as chaves do dicionário.
for n in nome.keys():  # esta forma é mais tradicional
    valor = nome[n]
    print(n, valor)

#  outra forma mais direta

for n, valor in nome.items():
    print(n, "=", valor)
