print('-'*30)
print('1051 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1052 - Mês')
# Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

N = int(input())
if N == 1:
    print('January')
elif N == 2:
    print('February')
elif N == 3:
    print('March')
elif N == 4:
    print('April')
elif N == 5:
    print('May')
elif N == 6:
    print('June')
elif N == 7:
    print('July')
elif N == 8:
    print('August')
elif N == 9:
    print('September')
elif N == 10:
    print('October')
elif N == 11: 
    print('November')
elif N == 12: 
    print('December')


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1053 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1054 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1055 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1056 - ')
#


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1057 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1058 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1059 - Números pares')
# Faça um programa que mostre os números pares entre 1 e 100, inclusive.
# Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

for i in range(2, 101):
    if i % 2 == 0:
        print(i)

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1060 - ')
# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

val = 0
for i in range(6):
    n = float(input())
    if n == 0:
        val = 0
    elif n > 0:
        val += 1
print(f'{val} valores positivos')

# ----------------------------------------------------------------------------------------------------------------

