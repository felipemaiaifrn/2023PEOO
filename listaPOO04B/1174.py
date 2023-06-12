x=[]
for l in range(100) :
  n = float(input())
  x.append(n)
  if n <= 10 : print(f'A[{l}] = {x[l]:.1f}')