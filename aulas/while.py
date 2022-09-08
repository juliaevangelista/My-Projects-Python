"""
while em python - aula 7
ultilizado para realizar ações enquanto uma condição for verdadeira
requisitos: entender condições e operadores


x=0
while x<10:
    if x==3:
     x+=1
     break # ou continue
    print(x)
    x+=1
print('acabou')


x = 0 # coluna

while x<10:
    y = 0 # linha
    while y<5:
        print(f'({x},{y})')
        y+=1
    x+=1
"""
# calculadora
while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    # + - * /
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número. ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)


    if operador == '+':
        print(num_1 +num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '*':
        print(num_1*num_2)
    elif operador == '/':
        print(num_1/num_2)
    else:
        print('Operador inválido.')
    


