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
  __med = []
  
  @classmethod
  def inserir(cls, m):
    NMedicamento.abrir()
    id = 0 
    for med in cls.__med:
      if med.get_id() > id: id = med.get_id()
    m.set_id(id + 1)
    cls.__med.append(m)  
    NMedicamento.salvar()

  @classmethod
  def listar(cls):
    NMedicamento.abrir()    
    return cls.__med

  @classmethod
  def listar_id(cls, id):
    NMedicamento.abrir()
    for med in cls.__med:
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
    cls.__med.remove(med)    
    NMedicamento.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__med = []
      with open("medicamentos.json", mode="r") as f:
        s = json.load(f)
        for med in s:
          c = Medicamento(med["_Medicamento__id"], med["_Medicamento__descricao"],
                     med["_Medicamento__valor"], med["_Medicamento__vencimento"])
          cls.__med.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("medicamentos.json", mode="w") as f:
      json.dump(cls.__med, f, default=vars)