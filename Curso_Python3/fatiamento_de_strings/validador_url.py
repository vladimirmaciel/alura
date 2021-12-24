import re

url = 'https://www.bytebank.com.br/cambio'
url_base = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = url_base.match(url)

if not match:
    raise ValueError("A URL não é valida")

print("A URL é valida")
