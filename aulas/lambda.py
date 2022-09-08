# def funcao(arg, arg2):
#     return arg * arg2
# var = funcao(2,2)
# print(var)

# a = lambda x, y : x * y
# print(a(2,2))

lista =[
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8]
]
print(sorted(lista, key=lambda i : i[1])) 



# ordem decrescente --> reverse=True

# lista.sort(key=lambda item :item[1])