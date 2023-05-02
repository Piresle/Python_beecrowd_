print('1006 - Média 2')
# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

A = float(input())
B = float(input())
C = float(input())
MEDIA = ((A*2)+(B*3)+(C*5)) / 10
print(f'MEDIA = {MEDIA:.1f}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1007 - Diferença')
# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = ((A*B)-(C*D))
print(f'DIFERENCA = {DIFERENCA}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1008 - Salário')
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

A = int(input())
B = int(input())
C = float(input())
SALARY = B * C
print(f'NUMBER = {A}')
print(f'SALARY = U$ {SALARY:.2f}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1009 - Salário com Bônus')
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nome = str(input())
salfixo = float(input())
totvendas = float(input())
bonus = float(totvendas * (15/100))
tot = salfixo + bonus
print(f'TOTAL = R$ {tot:.2f}')
# ----------------------------------------------------------------------------------------------------------------

print('-'*30)
print('1010 - Cálculo Simples')
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

p1 = input().split(" ")
p2 = input().split(" ")
cod1, qtde1, valor1 = p1
cod2, qtde2, valor2 = p2
total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))
print(f'VALOR A PAGAR: R$ {total:.2f}')          
# ----------------------------------------------------------------------------------------------------------------
