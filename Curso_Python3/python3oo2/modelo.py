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


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        # super().__init__(programas)  # setando uma lista de programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
temp = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

temp.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
# vingadores.nome = "harry potter"


atlanta.dar_likes()
atlanta.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, temp]
playlsit_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlsit_fim_de_semana)}')

print(len(playlsit_fim_de_semana))

for programa in playlsit_fim_de_semana.listagem:
    print(programa)

print(f'Tá ou não tá? {demolidor in playlsit_fim_de_semana}')

print(vingadores in playlsit_fim_de_semana)
print(playlsit_fim_de_semana[1])
