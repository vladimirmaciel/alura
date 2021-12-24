import re
endereco = "Rua Bacharel Floriano Ivo,87, Farol, Maceió, AL, 57055010"

# import re # Regular Expression -- RegEx

padrao = re.compile(
    "[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)  # Match
# print(busca)
if busca:
    cep = busca.group()
    print(cep)
