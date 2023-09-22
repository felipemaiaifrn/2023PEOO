import datetime
import json

class Medicamento:
  def __init__(self, id, desc, valor, vencimento):
    self.__id = id
    self.__desc = desc
    self.__valor = valor
    self.__vencimento = vencimento

  def set_id(self, id): self.__id = id
  def set_desc(self, desc): self.__desc = desc
  def set_valor(self, valor): self.__valor = valor
  def set_vencimento(self, vencimento): self.__vencimento = vencimento

  def get_id(self): return self.__id
  def get_desc(self): return self.__desc
  def get_valor(self): return self.__valor
  def get_vencimento(self): return self.__vencimento

  def __str__(self):
    return f"{self.__id} - {self.__desc} - {self.__valor} - {self.__vencimento}"



class NMedicamento:
  __listamed = []
  
  @classmethod
  def inserir(cls, m):
    NMedicamento.abrir()
    id = 0 
    for med in cls.__listamed:
      if med.get_id() > id: id = med.get_id()
    m.set_id(id + 1)
    cls.__listamed.append(m)  
    NMedicamento.salvar()

  @classmethod
  def listar(cls):
    NMedicamento.abrir()    
    return cls.__listamed

  @classmethod
  def listar_id(cls, id):
    NMedicamento.abrir()
    for med in cls.__listamed:
      if med.get_id() == id: return med
    return None

  @classmethod
  def atualizar(cls, m):
    NMedicamento.abrir()
    med = cls.listar_id(m.get_id())
    med.set_descricao(m.get_descricao())
    med.set_valor(m.get_valor())
    med.set_vencimento(m.get_vencimento())
    NMedicamento.salvar()

  @classmethod
  def excluir(cls, m):
    NMedicamento.abrir()
    med = cls.listar_id(m.get_id())
    cls.__listamed.remove(med)    
    NMedicamento.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__listamed = []
      with open("medicamentos.json", mode="r") as f:
        s = json.load(f)
        for med in s:
          c = Medicamento(med["_Medicamento__id"], med["_Medicamento__descricao"],
                     med["_Medicamento__valor"], med["_Medicamento__vencimento"])
          cls.__listamed.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("medicamentos.json", mode="w") as f:
      json.dump(cls.__listamed, f, default=vars)

class UI:
  @classmethod
  def Main(cls):
    op = 99
    while(op != 0):
      op = UI.Menu()
      if op == 1: UI.MedInserir()
      if op == 2: UI.MedListar()
      if op == 3: UI.MedAtualizar()
      if op == 4: UI.MedExcluir()
      if op == 5: UI.MedVencidos()

  @classmethod
  def Menu(cls):
    print("\nOpções: ")
    print("\n1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Vencidos")
    print("\n0 - Sair")
    return int(input())

  @classmethod
  def MedInserir(cls):
    descricao = input("Descrição: ")
    valor = input("Valor: ")
    data_str = input("Vencimento: ")
    data = datetime.datetime.strptime(data_str, '%d/%m/%Y')
    med = Medicamento(0, descricao, valor, data)
    NMedicamento.inserir(med)

  @classmethod
  def MedListar(cls):
    for med in NMedicamento.listar():
      print(med)

  @classmethod
  def MedAtualizar(cls):
    UI.MedListar()
    id = int(input("Id do medicamento a ser atualizado: "))
    desc = input("Nova descrição: ")
    valor = input("Novo valor: ")
    vencimento = input("Novo vencimento: ")
    med = Medicamento(id, desc, valor, vencimento)
    NMedicamento.atualizar(med)   

  @classmethod
  def MedExcluir(cls):
    UI.MedListar()
    id = int(input("Id do medicamento a ser excluído: "))
    med = Medicamento(id, "", "", "")
    NMedicamento.excluir(med)

UI.Main()