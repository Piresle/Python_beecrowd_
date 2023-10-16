print('-'*30)
print('1041 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1042 - Sort Simples')
## Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos. 1042

valores = list(map(int, input().split())) # digitar todos os valores na mesma linha 

for valor in sorted(valores):
    print(valor)

print("")

for valor in valores:
    print(valor)

# ERRO
'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 < n2) and (n1 < n3):
    if (n2 < n3):
        print(n1, n2, n3)
elif (n2 < n1) and (n2 < n3):
    if (n1 < n3):
        print(n2, n1, n3)
    elif (n3 < n1):
        print(n2, n3, n1)
elif (n3 < n1) and (n3 < n2):
    if (n1 < n2):
        print(n3, n1, n2)
    elif (n2 < n1):
        print(n3, n2, n1)
'''

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1043 - Triângulo')
# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X

A, B, C = map (float, input().split())
perimetro = A + B + C 
area = (A + B) * C/2 
if (A < (B + C)) and (B < (A + C)) and (C < (A + B)):
    print(f'Perimetro = {perimetro:.1f}')
else: 
    print(f'Area = {area:.1f}')

#  um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1044 - Múltiplos')
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

x = input().split()
a, b = x
a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if a == b:
    print('Sao Multiplos')

""" [ERRO]
A, B = map(int, input().split())
if ((B % A == 0) or (B % A == 0)):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
"""

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1045 - Tipos de Triângulos')
# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
""" se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES """

X, Y, Z = map (float, input().split())
if (X >= Y) and (X >= Z):
    A = X
    B = Y
    C = Z
if (Y >= X) and (Y >= Z):
    A = Y
    B = X
    C = Z
if (Z >= X) and (Z >= Y):
    A = Z
    B = X
    C = Y

if (A >= (B + C)):
    print('NAO FORMA TRIANGULO')
elif ((A*A) == ((B*B) + (C*C))):
    print('TRIANGULO RETANGULO')
elif ((A*A) > ((B*B) + (C*C))):
    print('TRIANGULO OBTUSANGULO')
elif ((A*A) < ((B*B) + (C*C))):
    print('TRIANGULO ACUTANGULO')   
if (A == B and B == C):
    print('TRIANGULO EQUILATERO')
elif ((A == B) or (B == C)):
    print('TRIANGULO ISOSCELES')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1046 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1047 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1048 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1049 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1050 - DDD')
#Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
# 61 - Brasília 
# 71 - Salvador
# 11 - São Paulo
# 21 - Rio de Janeiro
# 32 - Juiz de Fora
# 19 - Campinas 
# 17 - Vitoria
# 31 - Belo Horizonte
# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar: "DDD nao cadastrado"

ddd = int(input())
if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
# ----------------------------------------------------------------------------------------------------------------

