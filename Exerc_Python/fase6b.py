n1 = input('Digite algo: ')
print(type(n1))
print(n1.isnumeric())  # mesmo se for string ele mostra se é número
print(n1.isalpha())  # se é letra
print(n1.isalnum())  # se é alfanumérico - serve para somente números ou somente letras também
print(n1.isascii())
print(n1.isdecimal())
print(n1.isdigit())
print(n1.isidentifier())
print(n1.islower())  # se é composto somente por letras minúsculas
print(n1.isupper())  # se é composto somente por letras maiúsculas
print(n1.isprintable())
print(n1.isspace())  # se só tem espaços
print(n1.istitle())  # se está capitalizado
