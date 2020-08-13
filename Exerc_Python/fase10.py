'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
print('fim')

# jeito mais fácil

print('Seu carro é novo' if tempo <=3 else 'Seu carro é antigo')

nome = str(input('Qual é seu nome? '))

if nome.lower() == 'lucas':
    print('Deu certo!')
else:
    print('Deu certo também!')
print(f'Bom dia, {nome}!') '''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'Sua média é {m :.2f}')
if m <6:
    print('Sua média é vermelha')
else:
    print('Sua média é azul')