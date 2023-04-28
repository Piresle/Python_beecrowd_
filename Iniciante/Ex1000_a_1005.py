print("1000 - Hello World!")
# "O seu primeiro programa em qualquer linguagem de programação normalmente é o 'Hello World!'"

print("Hello World!")
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1001 - Extremamente Básico')
# "Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo."

A = int(input())
B = int(input())
X = A + B
print(f'X = {X}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1002 - Área do Cículo')
# "A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
    # Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
    # A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
    # Apresentar a mensagem "A=" seguido pelo valor da variável area com 4 casas após o ponto decimal."

n = 3.14159
raio = float(input())
area = n * (raio**2)
print(f'A={area:.4f}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1003 - Soma Simples')
# Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

A = int(input())
B = int(input())
SOMA = A + B
print(f'SOMA = {SOMA}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1004 - Produto Simples')
# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

A = int(input())
B = int(input())
PROD = A * B
print(f'PROD = {PROD}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1005 - Média 1')
# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

A = float(input())
B = float(input())
MEDIA = ((A*3.5) + (B*7.5)) / 11 
print(f'MEDIA = {MEDIA:.5f}')
# ----------------------------------------------------------------------------------------------------------------
