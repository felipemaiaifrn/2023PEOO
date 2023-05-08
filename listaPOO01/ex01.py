import math
class Circulo:
  def __init__(self):      #definindo dados do objeto
    self.pi = math.pi      #atributos
    self.r = 0           
  def calc_area(self):      #definindo operações do objeto
    return self.pi * self.r ** 2      #método
  def calc_circ(self):
    return self.pi * self.r * 2

x = Circulo()
x.r = float(input('Raio do círculo: '))
print(x.calc_area())
print(x.calc_circ())