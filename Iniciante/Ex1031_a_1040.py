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
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])
if (B > C) and (D > A) and ((C+D) > (A+B)) and (C > 0) and (D > 0) and ((A%2) == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1036 - Fórmula de Bhaskara')
# Leia 3 valores de ponto flutuante (A, B e C) e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

ent = input().split()
A = float(ent[0])
B = float(ent[1])
C = float(ent[2])
delta = (B**2) - (4*A*C)
if (A == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    X1 = (-B + (delta**(1/2))) / (2*A)
    X2 = (-B - (delta**(1/2))) / (2*A)
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')

# ERRO
'''
from math import sqrt 

ent = input().split()
A = float(ent[0])
B = float(ent[1])
C = float(ent[2])
delta = (B**2) - (4*A*C)
if (A == 0) or (delta < 0):
    print("Impossível calcular")
else:
    X1 = (-B + (sqrt(delta))) / (2*A)
    X2 = (-B - (sqrt(delta))) / (2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
'''

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
print('1040 - Média 3')
# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".
# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno. Todas as respostas devem ser apresentadas com uma casa decimal. 

A,B,C,D = map(float,input().split())
A = (A*2+B*3+C*4+D*1)/10
print(f'Media: {A:.1f}')
if A>=7.0:
    print("Aluno aprovado.")
elif A<5.0:
    print("Aluno reprovado.")
elif A>=5.0 and A<7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (A+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')

# ERRO
'''
N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())
media = (N1 + N2 + N3 + N4) / 4
print(f'Media: {media:.1f}')
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    ex = float(input())
    mf = (media+ex)/2
    print(f'Nota do exame: {ex:.1f}')
    if mf >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {mf:.1f}')
'''
# ----------------------------------------------------------------------------------------------------------------
