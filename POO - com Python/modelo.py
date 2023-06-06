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
    def nome(self, novo_nome):
         self._nome = novo_nome.title()

    def imprime(self):
        print(f'Nome: {self.nome}, Ano: {self.ano}, Likes: {self.likes}')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'Nome: {self.nome}, Ano: {self.ano}, Duração: {self.duracao}, Likes: {self.likes}')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas

    def imprime(self):
        print(f'Nome: {self.nome}, Ano: {self.ano}, {self.temporada} temporadas, Likes: {self.likes}')


vingadores = Filme("vingadores ultimato", 2018, 60)
vingadores.dar_likes()


gotham = Serie("Gotham city", 2012, 10)
gotham.dar_likes()
gotham.dar_likes()

filmes_e_series = [vingadores, gotham]

for programa in filmes_e_series:
    programa.imprime()