"""
Split, join, enumerate em Python
 * Split - dividir uma string # str
 * Join - juntar uma lista # str
 * Enumerate - enumerar elementos da lista # list

"""
cpf = '1.6.8.9.9.5.3.5.0'
lista = cpf.split('.')
print(lista)
for lista, r in enumerate(range(10,0,-1)):
    print(lista, r)