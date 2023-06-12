class Disciplina :
  def __init__(self) :
    self.__nome = 'Nome'
    self.__n1 = 0
    self.__n2 = 0
    self.__n3 = 0
    self.__n4 = 0
    self.__pf = 0
    
  def set_nome (self, nome) :
    self.__nome = nome
    
  def get_nome(self) :
    return self.__nome
    
  def set_n1(self, n) :
    if n <0 or n > 100 : raise ValueError()
    else : self.__n1 = n   
  def get_n1(self) :
    return self.__n1
  def set_n2(self, n) :
    if n <0 or n > 100 : raise ValueError()
    else : self.__n2 = n
  def get_n2(self) :
    return self.__n2
  def set_n3(self, n) :
    if n <0 or n > 100 : raise ValueError()
    else : self.__n3 = n
  def get_n3(self) :
    return self.__n3
  def set_n4(self, n) :
    if n <0 or n > 100 : raise ValueError()
    else : self.__n4 = n
  def get_n4(self) :
    return self.__n4
  def set_pf(self, n) :
    if n <0 or n > 100 : raise ValueError()
    else : self.__pf = n
  def get_pf(self) :
    return self.__pf

  def media_parcial(self):
    return (self.__n1*2+self.__n2*2+self.__n3*3 + self.__n4*3) / 10
    
  def media_final(self):
    return (self.media_parcial() + self.__pf) / 2
    
  def __str__(self) :
    return f'\nNome: {self.__nome}\nMédia parcial: {self.media_parcial():.2f}\nMédia final: {self.media_final():.2f}'

class UI:
  def main() :
    nome_disciplina = input('Nome: ')
    n1 = int(input('N1:'))
    n2 = int(input('N2:'))
    n3 = int(input('N3:'))
    n4 = int(input('N4:'))
    pf = int(input('Prova Final:'))
    x = Disciplina()
    
    x.set_nome(nome_disciplina)
    x.set_n1(n1)
    x.set_n2(n2)
    x.set_n3(n3)
    x.set_n4(n4)
    x.set_pf(pf)
    print(x)

UI.main()