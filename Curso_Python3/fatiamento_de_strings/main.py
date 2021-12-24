url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

# find para encontrar o índice de um caractere dentro de uma string, como em url.find("?") ,
# o método find tem a seguinte estrutura: str.find(sub[, start[, end]])
indicie_interogacao = url.find('?')

url_base = url[0:indicie_interogacao]
print(url_base)

tamanho = len(url)

# deixando após : em branco ele trás até o último caracter
url_paramento = url[indicie_interogacao+1:tamanho+1]

print(url_paramento)
url_paramento = url[indicie_interogacao+1:]
print(url_paramento)
# print(url)
