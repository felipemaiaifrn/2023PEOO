class Bingo:
  def __init__(self):
      self.__bolas = []
      self.__sorteados = []
  
  def iniciar(self, num_bolas):
      self.__bolas = list(range(1, num_bolas + 1))
  
  def proximo(self):
      if len(self.__bolas) > 0:
          indice_sorteado = self.__sorteados[-1] + 1 if self.__sorteados else 0
          bola_sorteada = self.__bolas[indice_sorteado]
          self.__bolas[indice_sorteado] = None
          self.__sorteados.append(bola_sorteada)
          return bola_sorteada
      else:
          return None
  
  def sorteados(self):
      return self.__sorteados
