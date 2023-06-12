import math
class Circulo :
  def __init__(self) :
    self.__raio = 0
    self.__pi = math.pi
  def set_raio(self, r) :
    if r >= 0 : self.__raio = r
    else : raise ValueError()
  def gat_raio (self) :
    return self.__raio
  def calc_area (self) :
    area = self.__pi * (self.__raio ** 2)
    return area
  def calc_circ (self) :
    return 2 * self.__pi * self.__raio
  def __str__(self) :
    return f'Área do círculo: {self.calc_area():.2f}\nCircunferência do círculo: {self.calc_circ():.2f}'

class UI :
  def main() :
    raio = int(input('Valor do raio: '))
    x=Circulo()
    x.set_raio(raio)
    print(x)

UI.main()