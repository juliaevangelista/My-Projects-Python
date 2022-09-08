"""
Faça um programa que peça ao usúario para digitar um número 
inteiro, informe se este número é ímpar ou par.
Caso o usúario não digite um número inteiro, informe que não 
é um número inteiro

try:
    num = input('Informe um número inteiro: ')
    num = int(num)
    if num%2==0:
       print('Par.')
    elif num%2==1:
       print('Ímpar')
except:
    print('Este número não é inteiro')
"""

"""
Faça um programa que pergunte a hora ao usúario e, 
baseando-se no horário descrito, exiba a saudação apropriada:
Bom dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23

try:
 hora = int(input('Digite um horario (0-23): '))
 if hora>=0 and hora<=11:
    print('Bom dia.')
 elif hora>=12 and hora<=17:
    print('Boa Tarde.')
 elif hora>=18 and hora<=23:
    print('Boa Noite.')
except:
    print('Valor inválido. ')
""" 

"""
Faça um programa que peça o primeiro nome do usúario. Se o
nome tiver 4 letras ou menos escreva "Seu nome é muito curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande".

nome = input('Escreva seu nome: ')
carac = nome.__len__()
if carac>=0 and carac<= 4:
    print("Seu nome é muito curto")
elif carac >=5 and carac <= 6:
    print("Seu nome é normal")
elif carac > 6:
    print("Seu nome é muito grande")
else:
    print('Valor inválido')
"""