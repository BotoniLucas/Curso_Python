# desafio 15

c = float(input('Digite a temperatura em ºC: '))
f = (c*9/5)+32
k = c+273.15
print('A temperatura é de {}ºF e {}K' .format(f, k))

# desafio 15

km = float(input('Digite quantos Km o carro percorreu: '))
dias = float(input('Digite por quantos dias alugou o carro: '))
aluguel = (dias*60)+(km*0.15)
print('O valor a pagar é de R${:.2f}' .format(aluguel))