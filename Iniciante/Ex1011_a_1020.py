print('-'*30)
print('1011 - Esfera')
# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

R = float(input())
pi = 3.14159
vol = (4/3.0) * pi * (R)**3
print(f'VOLUME = {vol:.3f}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
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
Erro (variáveis sem lista)
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
print('-'*30)
print('1013 - O Maior')
# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula: MaiorAB = (a+b+abs(a-b)) / 2
# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a+b+abs(a-b)) / 2
maiorC = (maiorAB + c + abs(maiorAB - c)) / 2
maiorC = int(maiorC)
print(f'{maiorC} eh o maior')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1014 - Consumo')
# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

X = int(input())
Y = float(input())
cons = X / Y
print(f'{cons:.3f} km/l')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1015 - Distância Entre Dois Pontos')
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula: 
# Distancia = raiz(x2-x1)² + (y2-y1)²

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
print(f'{distancia:.4f}')


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1016 - Distância')
# Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.
# Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.
# Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

d = int(input())
tempo = d * 2
print(f'{tempo} minutos')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1017 - Gasto de Combustível')
# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

tempo = int(input())
vel = int(input())
li = 12
dist = tempo * vel 
litros = dist / 12
print(f'{litros:.3f}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1018 - Cédulas')
# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.


# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1019 - Conversão de Tempo')
# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

N = int(input())
horas = N // (60*60)
N = N % (60*60)
minutos = N // 60
N = N % 60
print(f'{horas}:{minutos}:{N}')

# ----------------------------------------------------------------------------------------------------------------
print('-'*30)
print('1020 - Idade em Dias')
# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

idade = int(input())
ano = idade // 365
mes = (idade % 365) // 30 
dia = (idade % 365) % 30
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')

# ----------------------------------------------------------------------------------------------------------------
