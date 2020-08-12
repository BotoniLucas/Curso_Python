# desafio 22

nome = str(input('Digite o seu nome completo: ')).strip()
# nome = 'Lucas Botoni de Souza'
print(nome.upper()) # todas em maiúsculo
print((nome.lower())) # todas em minúsculo
print(len(nome)-nome.count(' ')) # numero total de letras (sem os espaços)
print(nome[0])) # primeiro nome
print(len(nome[0])) # quantas letras tem o primeiro nome ou nome.find(' ') - tudo antes do primeiro espaço

# desafio 23

num = int(input('Digite um número inteiro de 0 a 9999: '))
nums = str(num)
print(f' Unidade: {nums[3] :2} \n Dezena: {nums[2] :2} \n Centena: {nums[1] :2} \n Milhar: {nums[0] :2} \n')
# outro jeito
u = num//1%10
d = num//10%10
c = num//10%10
m = num//1000%10
print(f' Unidade: {u :2} \n Dezena: {d :2} \n Centena: {c :2} \n Milhar: {m :2} \n') # :2 - cada numero ocupa 2 espaços

# desafio 24

nome = str(input('Digite o nome da cidade: ')).strip()
print('santo' in nome[:5].lower()) # ou nome[:5] == 'santo'

# desafio 25

nome = str(input('Digite o seu nome completo: ')).strip()
print('silva' in nome.lower())

# desafio 26

# frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed'
frase = str(input('Digite uma frase: ')).strip().lower()
print('a letra A aparece {} vezes na frase' .format(frase.count('a')))
print(frase.find('a')) # primeira aparição de 'a'
print(frase.rfind('a')) # última aparição de 'a'

# desafio 27
nome = str(input('Digite o seu nome completo: ')).strip().split()
# nome = 'Lucas Botoni de Souza'
print(f'primeiro nome: {nome[0]}')
print(f'ùltimo nome: {nome[len(nome)-1]}')
