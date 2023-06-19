from math import sqrt 

A, B, C = map(str(input()).split())
A = float(A)
B = float(B)
C = float(C)
delta = (B**2) - (4*A*C)
if A == 0:
    print("Impossível Calcular")
else:
    R1 = (-B + (delta**(1/2))) / (2*A)
    R2 = (-B - (delta**(1/2))) / (2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
