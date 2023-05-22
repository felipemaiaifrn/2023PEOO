class Frete:
  def __init__(self, d, p) :
    self.__d = d
    self.__p = p
  def set_distancia (self, d):
    if self.__d >= 0 : return d
    else: raise ValueError()
  def set_peso (self, p) :
    if self.__p >= 0 : return p
    else : raise ValueError()
  def get_distancia(self) :
    return self.__d
  def get_peso(self) :
    return self.__p
  def calc_frete(self) :
    frete = (self.__d * self.__p) * 0.01
    return frete
  def __str__(self) :
    return f'Peso(Kg): {self.__p} | Distância(Km): {self.__d} | Frete: {self.calc_frete()}
    