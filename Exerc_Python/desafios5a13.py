# desafio 5

n5 = int(input('Digite um número: '))
print('O antecessor de {} é {}, seu sucessor é {}' .format(n5, (n5-1), (n5+1)))

# desafio 6

n6 = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo de {} é {}, a raiz quadrada de {} é {:.3f}' .format(n6, (n6*2), n6, (n6*3), n6, (n6**(1/2)))) # ou raiz = sqrt(3)

# desafio 7

n71 = float(input('Digite a primeira nota: '))
n72 = float(input('Digite a segunda nota: '))
print('A média é {:.2f}' .format((n71+n72)/2))

# desafio 8

n8 = int(input('Digite um valor em metros: '))
print('O valor em centímetros de {}m é {}cm \n O Valor em milímetros de {}m é {}mm' .format(n8, (n8*100), n8, (n8*1000)))

# desafio 9

n9 = int(input('Digite qual tabuada quer saber: '))
print(' {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}' .format(n9*1, n9*2, n9*3, n9*4, n9*5, n9*6, n9*7, n9*8, n9*9, n9*10)) # antigo


# desafio 10

n10 = float(input('Quantos reais você tem na carteira? O dólar hoje está valendo R$5,41: '))
print('Com R${:.2f} você pode comprar US${:.2f}' .format(n10, (n10/5.41)))

# desafio 11

n111 = float(input('Digite a largura: '))
n112 = float(input('Digite a altura: '))
a = n111*n112
print('Você precisa de {:.2f} L de tinta para uma área de {}m²' .format((a/2), a))

# desafio 12

n12 = float(input('Digite o preço do produto: '))
print('O preço do produto com desconto de 5% é {}' .format(n12*0.95))

# desafio 13

n13 = float(input('Digite o salário do funcionário: '))
print('O preço do produto com aumento de 15% é {}' .format(n12*1.15))