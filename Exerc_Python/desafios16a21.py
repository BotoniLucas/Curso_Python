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