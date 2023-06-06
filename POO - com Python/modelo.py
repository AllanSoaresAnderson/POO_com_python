class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    def dar_likes(self):
        self.__like += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def like(self):
        return self.__like

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()



class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.like = 0

    def dar_likes(self):
        self.like += 1


vingadores = Filme('vingadores ultimato', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.like}')


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.like}')