class PeçaDominó:
    def __init__(self, lado1, lado2):
      if lado1 < 0 or lado1 > 6:
        raise ValueError()
      if lado2 < 0 or lado2 > 6:
        raise ValueError()
      self.lado1 = lado1
      self.lado2 = lado2

    def combinar_com(self, outra_peca):
        return self.lado1 == outra_peca.lado1 or self.lado1 == outra_peca.lado2 or  self.lado2 == outra_peca.lado1 or self.lado2 == outra_peca.lado2

    def __str__(self):
        return f"Peça de dominó: [{self.lado1} | {self.lado2}]"


# Programa principal para testar a classe PeçaDominó
peca1_lado1 = int(input("Digite o valor do lado 1 da primeira peça: "))
peca1_lado2 = int(input("Digite o valor do lado 2 da primeira peça: "))
peca2_lado1 = int(input("Digite o valor do lado 1 da segunda peça: "))
peca2_lado2 = int(input("Digite o valor do lado 2 da segunda peça: "))

peca1 = PeçaDominó(peca1_lado1, peca1_lado2)
peca2 = PeçaDominó(peca2_lado1, peca2_lado2)

if peca1.combinar_com(peca2):
    print("As peças combinam.")
else:
    print("As peças não combinam.")