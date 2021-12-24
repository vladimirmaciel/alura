import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(sel, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        # url = 'https://www.bytebank.com.br/cambio'

        url_base = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_base.match(url)

        if not match:
            raise ValueError("A URL não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[: indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = (
    "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
extrator_url = ExtratorURL(url)
# extrator_url = ExtratorURL(None)
# extrator_url = ExtratorURL(
#     "cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91883")


valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)

# extrator_url = ExtratorURL("   ")
