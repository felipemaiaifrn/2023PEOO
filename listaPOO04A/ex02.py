import datetime

class Musica:
  def __init__(self, titulo, artista, album, datainclusao, duracao):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
    self.__datainclusao = datainclusao
    self.__duracao = duracao
  def get_duracao(self):
    return self.__duracao
  def __str__(self):
    return f"Título: {self.__título}, Artista: {self.__artista}, Álbum: {self.__álbum}, Data de inclusão: {self.__data_inclusão}, Duração: {self.__duração}"

class Playlist:
  def __init__(self, nome, descricao):
    self.__nome = nome
    self.__descricao = descricao
    self.__musicas = []
  def inserirmusicas (self, musica):
    self.__musicas.append(musica)
  def listarmusicas (self) :
    return self.__musicas
  def tempo_total (self) :
    duracao = datetime.timedelta()
    for m in self.__musicas :
      duracao += m.get_duracao()
    return duracao
  def __str__(self):
    return f"Nome: {self.__nome}, Descrição: {self.__descrição}"

class UI:
  @staticmethod
  