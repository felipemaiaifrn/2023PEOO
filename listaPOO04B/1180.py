N = int(input())
if N < 1 or N > 1000 : raise ValueError()
a = list(map(int, input().split(" ")))
x = []
for l in range(N) :
  x.append(a[l])
menor = min(x)
for m in range(N):
  if x[m] == min(x) : posicao = m
print(f'Menor Valor: {menor}')
print(f'Posição: {posicao}')