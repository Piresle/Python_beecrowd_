print('-'*30)
print('1061 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1062 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1063 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1064 - Positivos e Média')
# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.
# O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

pos = 0
soma = 0
for i in range(6):
    x = float(input())
    if (x > 0):
        pos += 1
        soma += x
media = soma / pos
print(f'{pos} valores positivos')
print(f'{media:.1f}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1065 - Pares entre Cinco Números')
# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

par = 0
for i in range(5):
    n = int(input())
    if (n % 2 == 0):
        par += 1 
print(f'{par} valores pares')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1066 - Pares, Ímpares, Positivos e Negativos')
# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

par = 0 
imp = 0
pos = 0 
neg = 0
for i in range(5):
    n = int(input())
    if (n % 2 == 0):
        par += 1
    elif (n % 2 != 0):
        imp += 1
    if (n > 0):
        pos += 1
    elif (n < 0):
        neg += 1
print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1067 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1068 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1069 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1070 - ')
#


# ----------------------------------------------------------------------------------------------------------------

