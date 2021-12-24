# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
url = "    "

#  Sanitização da URL
url = url.strip()  # tira os espaçoes em branco da URL
#  temos também lstrip e rstrip remove espaços em branco da esquera e da direita
# url = url.replace(" ", "") # trocar caracter por um outro

# validação da URL
if url == "":
    raise ValueError("A URL está vázia")

# Separa base e os parâmetros
indicie_interogacao = url.find('?')
url_base = url[:indicie_interogacao]
print(url_base)
url_paramento = url[indicie_interogacao+1:]
print(url_paramento)

# Busca o valor de um parâmetro
# parametro_busca = 'moedaOrigem'
# parametro_busca = 'moedaDestino'
parametro_busca = 'quantidade'
indice_parametro = url_paramento.find(parametro_busca)

# print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_paramento.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_paramento[indice_valor:]
else:
    valor = url_paramento[indice_valor:indice_e_comercial]

print(valor)
