# desafio 16
from math import trunc

n = float(input('Digite um número qualquer: '))
pi = trunc(n) # ou int(n)
print('A parte inteira de {:.2f} é {} ' .format(n, pi))

# desafio 17

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto ajdacente: '))
h = hypot(co, ca)
print(f'A hipotenusa de {ca} e {co} é {h :.1f}') # nova sintaxe

# desafio 18

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
ang = radians(ang)
print(f'O seno é {sin(ang) :.2f}, o cosseno é {cos(ang) :.2f} e a tangente é {tan(ang) :.2f}')

# desafio 19
import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]

ordem = random.choice(lista)
print(f'O aluno escolhido foi {ordem}')
