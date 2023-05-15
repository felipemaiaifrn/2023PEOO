import math
class circulo :
  def __init__(self):
    self.__raio = 0
    self.__pi = math.pi
  def set_raio(self, raio) :
    if self.__raio < 0 : raise ValueError()
    else : return self.__raio()
  def get_raio(self) :
    return self.__raio()
  def calc_area (self) :
    return self.__pi * self.__raio ** 2
  def calc_circ (self) :
    return self.__pi * self.__raio * 2

r = float(input())
x = circulo()
x.set_raio(r)
print(x.calc_area)
print(x.calc_circ)