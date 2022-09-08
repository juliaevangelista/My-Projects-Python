"""
Funções (def) em python - *args **kwargs - parte 3

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2= [10,20,30,40,50]
func(*lista, *lista2, nome = 'Luiz', sobrenome = 'Miranda', idade = 30)
"""
"""
PARTE 4
"""
def func():
    outra_variavel = 'Luiz Otávio'  # variável local
    return outra_variavel # retornando variavel local
def func2(arg): # ultilizando outra_variavel em arg
    print(arg) # dando print em outra_variavel
var = func() # chamando outra_variável
func2(var) 