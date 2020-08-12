print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam tempus felis felis, vitae dictum ipsum viverra ut. Etiam in fringilla ex. 
Sed vestibulum dui nisl, quis ultricies mi blandit vel. Aliquam ultricies eros vel arcu fringilla, nec condimentum odio malesuada. Donec aliquam justo et massa pretium, 
vitae posuere tortor suscipit. Fusce placerat commodo auctor. Cras nec diam turpis. Aliquam efficitur ante tortor, sed euismod felis sodales facilisis. Duis lacus risus, 
gravida sit amet mauris non, gravida porttitor nulla. Vestibulum convallis in magna a tincidunt. Orci varius natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Aliquam id felis consequat metus condimentum vulputate nec malesuada nunc. Aliquam porttitor fringilla mauris. Mauris consectetur, 
arcu et congue tempus, est lacus vehicula eros, sed aliquet risus mi vel velit. Phasellus eu risus sed nisi blandit tempor ac et metus.''') # aspas triplas para textos grandes

frase = 'curso em video python'
print(frase[::3]) # inicio até o final de 3 em 3
print(frase.count('o')) # conta quantos 'o' tem
print(frase.replace('python', 'bobobo')) # não dá pra alterar automaticamente como frase[0] = 'j' tem que ser frase = frase.replace...
print(frase.find('curso')) # igual o find do matlab - acha a primeira posição
print('curso' in frase) # retorna true se curso está contido em frase
print(frase.split()) # separa as palavras da frase pelo espaço

# usar também lower e upper, title e capitalize