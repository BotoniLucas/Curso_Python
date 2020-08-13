'''# desafio 28

import random
from time import sleep

adv = random.randrange(0, 5, 1) #ou randint
user = int(input('Qual número de 1 a 5 o computador escolheu? '))
print('Processando...")
sleep(2) # espera 2 segundos
print(f'O número do computador foi {adv}')
if user == adv:
    print('Você acertou!')
else:
    print('Você errou') '''

'''# desafio 29

vel = float(input('Qual a velocidade do carro? '))
if vel >80:
    print(f'Você ultrapassou o limite de 80km/h, sua multa é de R${(vel-80)*7 :.2f}')
else:
    print('Você está dentro do limite') '''

''' # desafio 30

n = int(input('Digite um número inteiro: '))
if n%2 == 0:
    print('O número é par')
else:
    print('O número é ímpar') '''

''' # desafio 31

d = float(input('Digite a distância da viagem em Km: '))
if d <=200:
    print(f'O preço da viagem é de R${d*0.5 :.2f}')
else:
    print(f'O preço da viagem é R${d*0.45 :.2f}') '''

''' # desafio 32
from datetime import date
ano = int(input('Digite o ano. Para o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if (ano%4==0) and (ano%100)!=0 or (ano%400)==0: # também pode usar and e or como & e barra reta
    print(f'O ano de {ano} é bissexto: ')
else:
    print(f'O ano de {ano} não é bissexto: ') '''

'''# desafio 33

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
# para o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# para o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é {maior :.2f} e o menor é {menor :.2f}') '''

'''# desafio 34

sal = float(input('Digite o salário: '))
if sal>1250:
    print(f'O novo salário é de {sal*1.1 :.2f}')
else:
    print(f'O novo salário é de {sal*1.15 :.2f}') '''

 # desafio 35

n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o o comprimento da terceira reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print(f'Os segmentos {n1}, {n2} e {n3} podem formar um triângulo')
else:
    print(f'Os segmentos {n1}, {n2} e {n3} não podem formar um triângulo')


