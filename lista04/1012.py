ABC=input().split()
pi = 3.14159
A=float(ABC[0])
B=float(ABC[1])
C=float(ABC[2])
a_tri=A*C/2
a_circulo=pi*(C**2)
a_trap=(A+B)/2*C
a_quad=B*B
a_ret=A*B
print(f'TRIANGULO: {a_tri:.3f}')
print(f'CIRCULO: {a_circulo:.3f}')
print(f'TRAPEZIO: {a_trap:.3f}')
print(f'QUADRADO: {a_quad:.3f}')
print(f'RETANGULO: {a_ret:.3f}')