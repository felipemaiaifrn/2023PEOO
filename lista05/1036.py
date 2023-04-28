A, B, C = map(float, input().split())
delta=B**2-4*A*C
x1=(-B+delta**0.5)/2*A
x2=(-B-delta**0.5)/2*A
print(f'R1 = {x1/100:.5f}')
print(f'R2 = {x2/100:.5f}')