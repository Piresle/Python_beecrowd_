print('-'*30)
print('1071 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1072 - Intervalo 2')
# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

N = int(input())
inx = 0
outx = 0
for i in range(N):
    X = int(input())
    if (20 >= X >= 10):
        inx += 1
    else: 
        outx += 1
print(f'{inx} in')
print(f'{outx} out')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1073 - Quadrado de Pares')
# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

n = int(input())
x = 2
for i in range(2 , n+1 , 2):
    print(f'{i}^2 = {i**2}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1074 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1075 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1076 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1077 - ')
# 


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1078 - Tabuada')
# Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:  

N = int(input())
if 2 < N < 1000:
    for cont in range(1, 11):
        print(f'{cont} x {N} = {N*cont}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1079 - Médias Ponderadas')
# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1080 - ')
# 


# ----------------------------------------------------------------------------------------------------------------