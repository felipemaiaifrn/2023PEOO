class Disciplina:
  def __init__(self, nome, n1, n2, n3, n4, PF):
    self.nome = nome
    self.n1 = n1
    self.n2 = n2
    self.n3 = n3
    self.n4 = n4
    self.PF = PF
  def media_parcial(self):
    media_parcial = (self.n1*2+self.n2*2+self.n3*3+self.n4*3) / 10
    return media_parcial
  def media_final(self):
    return (self.media_parcial() + self.PF) / 2
  def __str__(self):
    if self.media_parcial() >= 60:
      return f"Disciplina: {self.nome}\nMédia Parcial {self.media_parcial():.2f}\nSituação: Aprovado"
    elif self.media_final() >= 60:
      return f"Disciplina: {self.nome}\nMédia Parcial: {self.media_parcial():.2f}\nMédia Final: {self.media_final():.2f}\nSituação: Aprovado"
    else:
      return f"Disciplina: {self.nome}\nMédia Parcial: {self.media_parcial():.2f}\nMédia Final: {self.media_final():.2f}\nSituação: Reprovado"

nome = input('Nome: ')
n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
n4 = int(input('N4: '))
PF = int(input('Prova final: '))
x = Disciplina(nome, n1, n2, n3, n4, PF)
print(x)