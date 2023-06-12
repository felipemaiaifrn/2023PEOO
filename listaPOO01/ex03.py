class Viagem :
  def __init__(self, d, t) :
    self.distancia = d
    self.tempo = t
  def calc_vel(self) :
    vel = self.distancia / self.tempo
    return vel

distancia = float(input('Distância (km): '))
horas = float(input('Horas: '))
minutos = float(input('Minutos: '))
tempo = horas + minutos / 60
x = Viagem(distancia, tempo)
print(f'{x.calc_vel():.2f} km/h')