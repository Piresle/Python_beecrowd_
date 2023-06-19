print('-'*30)
print('1031 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1032 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1033 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1034 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1035 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1036 - ')
# Leia 3 valores de ponto flutuante (A, B e C) e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

from math import sqrt 

A = float(input())
B = float(input())
C = float(input())
delta = (B**2) - (4*A*C)
if A == 0:
    print("Impossível calcular")
elif delta < 0:
    print("Impossível calcular")
else:
    R1 = (-B + (sqrt(delta))) / (2*A)
    R2 = (-B - (sqrt(delta))) / (2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1037 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1038 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1039 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1040 - ')
#


# ----------------------------------------------------------------------------------------------------------------