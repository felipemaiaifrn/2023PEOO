n = int(input())
x = []
x.insert(0, n)
for l in range(10) :
  n *= 2
  x.append(n)
  print(f'N[{l}] = {x[l]}')