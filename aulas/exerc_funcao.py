"""
1 - Crie uma funcao que exibe uma saudacao com os parâmetros saudação e nome.

def funcao(saudacao, nome):
    print(f'{saudacao}, {nome}')

funcao('oi', 'julia')
funcao('oi', 'fulano')
"""

"""
2 - crie uma funcao que recebe 3 numeros como parametros e exiba a soma entre eles.

def funcao(n1= int(input('Digite um número: ')), n2= int(input('Digite outro número: ')), n3= int(input('Digite outro número: '))):

    return n1+n2+n3

valor = funcao()
print(f'Soma é {valor}')
"""

"""
3 - crie uma funcao que receba 2 números. o primeiro é um valor e o segundo um percentual (ex. 10%). retorne(return) o 
valor do primeiro número somado do aumento do percentual do mesmo.



def funcao(n1 = int(input('Digite um número: ')), p1=int(input('Digite um percentual: '))):
    return ((p1/100) * n1)+n1

valor = funcao()
print(f'O total é {valor}')
"""

"""
4 - Fizz Buzz - Se o parâmetro da função for divisivel por 3, retorne fizz, se o parâmetro da função for divisivel por 5,
retorne buzz. Se o parâmetro for divisivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado

"""
def funcao(num):
    if num%5==0 and num%3==0:
        return f'FizzBuzz = {num} é divisivel por 5 e 3'
    if num%3==0:
        return f'Fizz = {num} é divisivel por 3'
    if num%5==0:
        return f'Buzz= {num} é divisivel por 5'
    return num

from random import randint
for i in range(100):
    aleatorio = randint(0, 100)
    print(funcao(aleatorio))