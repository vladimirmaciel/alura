class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    '''
        com o __str__(), estamos definindo uma representação textual para o nosso objeto.
    '''

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - Likes: {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duraçã:{self.duracao}(minutos) - Likes: {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} -Temporadas:{self.temporadas} -  Likes: {self._likes} Likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.nome = "harry potter"

atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    print(programa)
