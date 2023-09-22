class Retangulo:

  def __init__(self, b, h):
    self.__b = b
    self.__h = h

  def set_base(self, b):
    if b >= 0: self.__b = b
    else: raise ValueError()

  def get_base(self):
    return self.__b

  def set_altura(self, h):
    if h >= 0: self.__h = h
    else: raise ValueError()

  def get_base(self):
    return self.__h

  def calc_area(self):
    return self.__b * self.__h

  def calc_diag(self):
    return ((self.__b**2) + (self.__h**2))**0.5

  def __str__(self):
    return f'Base: {self.__b} | Altura: {self.__h} | Área: {self.calc_area():.2f} | Diagonal: {self.calc_diag():.2f}'


class UI:

  @staticmethod
  def main():
    print('Informe a base e altura do retângulo:')
    base = float(input())
    altura = float(input())
    x = Retangulo(base, altura)
    print(x)


UI.main()