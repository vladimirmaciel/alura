usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
print(assistiram)
assistiram.extend(usuarios_machine_learning)
print(assistiram)
print(
    set(assistiram)
)  # Utilizando definição de conjuntos para exbir sem os elementos repeditos

# anotação para criar um conjunto simples é a chaves, conjunto não tem indexação não tem chave para localizar a posição  possui apenas os elementos

num = {1, 3, 4, 5, 6, 1}
print(num)


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

uniao = usuarios_data_science | usuarios_machine_learning  # uniao dos dois conjuntos
print(uniao)
