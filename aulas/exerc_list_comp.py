# string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
# n = 10
# lista = [string[i:i+n] for i in range(0, len(string),n)]
# retorno = '.'.join(lista)
# print(lista)
# print(retorno)

# carrinho = []

# carrinho.append(('Produto 1', 20))
# carrinho.append(('Produto 2', 30))
# carrinho.append(('Produto 3', 50))

# total=sum([y for x, y in carrinho])
# print(total)

lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4]
listas = [x + y for x, y in zip(lista1,lista2)]
print(listas)

