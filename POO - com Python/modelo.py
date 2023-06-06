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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas



vingadores = Filme("vingadores ultimato", 2018, 60)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, Likes: {vingadores.likes}')


gotham = Serie("Gotham city", 2012, 10)
gotham.dar_likes()
gotham.dar_likes()
print(f'Nome: {gotham.nome}, Ano: {gotham.ano}, Duração: {gotham.temporada}, Likes: {gotham.likes}')