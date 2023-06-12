class Triangulo :
  def __init__(self):
    self.__b = 0
    self.__h = 0
  def set_base(self, b) :
    if b >= 0 : self.__b = b
    else : raise ValueError()
  def get_base(self):
    return self.__b
  def set_altura(self, h):
    if h >= 0 : self.__h = h
    else : raise ValueError()
  def get_altura(self) :
    return self.__h
  def calc_area(self):
    area = (self.__b * self.__h) / 2
    return area

class UI:
  def main():
    x=Triangulo()
    b = float(input('Informe a base: '))
    h = float(input('Informe a altura: '))
    x.set_base(b)
    x.set_altura(h)
    print(x.get_base())
    print(x.get_altura())
    print(x.calc_area())
UI.main()