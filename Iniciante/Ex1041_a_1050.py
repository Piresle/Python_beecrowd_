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
print('1044 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1045 - ')
#


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

