print('1011 - Esfera')
# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

R = float(input())
pi = 3.14159
vol = (4/3.0) * pi * (R)**3
print(f'VOLUME = {vol:.3f}')
# ----------------------------------------------------------------------------------------------------------------

print('1012 - Área')
# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

a,b,c = list(map(float,input().split()))
triangle=0.5*a*c
circle=3.14159*c*c
trapezium=(a+b)/2.0*c
square=b*b
rectangle=a*b
print("TRIANGULO: %.3lf"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)

''' 
Erro (?)
A = float(input())
B = float(input())
C = float(input())
pi = 3.14159
atri = (A * C) / 2
acir = pi * (C**2)
atra = ((A + B) * C) / 2 
aqua = B ** 2
aret = A * B
print(f'TRIANGULO: {atri:.3f}')
print(f'CIRCULO: {acir:.3f}')
print(f'TRAPEZIO: {atra:.3f}')
print(f'QUADRADO: {aqua:.3f}')
print(f'RETANGULO: {aret:.3f}') 
'''

# ----------------------------------------------------------------------------------------------------------------

print('1013 - O Maior')
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula: MaiorAB = (a+b+abs(a-b)) / 2
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.


# ----------------------------------------------------------------------------------------------------------------

print('1014 - Consumo')
# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).


# ----------------------------------------------------------------------------------------------------------------

print('1015 - Distância Entre Dois Pontos')
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula: 
# Distancia = raiz(x2-x1)² + (y2-y1)²


# ----------------------------------------------------------------------------------------------------------------
