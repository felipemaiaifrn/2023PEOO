#NAO TERMINADO

class cinema:
  def __init__(self):
    self.__dia = "dom"
    self.__horario= 17
  def set_dia(self, dia) :          #self chama a função
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    if dia in dias: self.__dia = dia
    else: raise ValueError()
  def get_dia (self) :
    return self.__dia
  def set_horario(self, horario):
    if horario >= 0 and horario>= 23 : self.__horario = horario
  def get_horario(self) :
    return self.__horario
  def inteira():
    if self.__dia == "qua" : return 8
    valor = 20
    if self.__dia == "seg" or self.__dia == "ter" or self.__dia == "qui" : return 

class UI:
  @staticmethod   #chamar operação usando nome da classe, não atribuir objeto
  def main():
    x= cinema()
    x.set_dia("sex")
    x.set_horario(15)
    print(x.get_dia())
    print(x.get_horario())
    
UI.main()