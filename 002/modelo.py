class Filme:
    def __int__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

class Serie:
    def __int__(self,nome,ano,temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie("atlanta",2018,2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}'
      f'Temporadas: {atlanta.temporadas}')
