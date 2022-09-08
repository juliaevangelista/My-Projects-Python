"""
1 - crie uma função que recebe uma funcao2 como parâmetro e retorne o valor da funcao2 executada.
"""

# def funcao2():
#     argumento = 'Valor'
#     return argumento
# def funcao(arg):
#     print(arg)
# var = funcao2()
# funcao(var)

"""
2 - crie uma funcao1 que recebe funcao2 como parâmetro e retorne o valor da funcao2 executada. faça a funcao1 executar
2 funções que recebem um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)
def fala_oi(nome):
    return f'Oi {nome}' 
def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi,'Luiz')
executando2 = mestre(saudacao, 'João', saudacao='Bom dia')
print(executando)
print(executando2)

