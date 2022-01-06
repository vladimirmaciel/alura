usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

intersecao = usuarios_data_science & usuarios_machine_learning
print(intersecao)

fez_data_sciente_nao_fez_machine = usuarios_data_science - usuarios_machine_learning
print(fez_data_sciente_nao_fez_machine)

print(15 in fez_data_sciente_nao_fez_machine)

# ou exclusivo
print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))
usr = usuarios
usr.add(12)
print(len(usr))

usuarios = frozenset(usuarios)  # conj congelados, são imutaveis
print(usuarios)

palavra = (
    "meu nome é vladimir, meu filho é Davi, minha esposa Amanda e meu cacahrro luke"
)
quebra_palavra = palavra.split()
print(quebra_palavra)
quebra_palvara_set = set(quebra_palavra)
print(quebra_palvara_set)
