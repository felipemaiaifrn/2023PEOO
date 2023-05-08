class disciplina :
  def __init__(self):
    self.nome = 0
    self.n1 = 0
    self.n2 = 0
    self.n3 = 0
    self.n4 = 0
    self.provafinal = 0
  def media_parcial(self) :
    return (self.n1*2 + self.n2*2 + self.n3*3 + self.n4*3) / 10
  #def media_final :
mat=disciplina()
mat.n1 = 0
mat.n2 = 0
mat.n3 = 100
mat.n4 = 100
print(mat.media_parcial())