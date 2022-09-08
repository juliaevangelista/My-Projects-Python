perguntas = {
    'Pergunta 1' : {
        'pergunta': 'quanto é 2+2',
        'respostas':{'a' : '1','b' : '4','c' : '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2' : {
        'pergunta': 'quanto é 2+1',
        'respostas':{'a' : '1','b' : '4','c' : '3',},
        'resposta_certa': 'c',
    },
    'Pergunta 3' : {
        'pergunta': 'quanto é 2+3',
        'respostas':{'a' : '1','b' : '4','c' : '5',},
        'resposta_certa': 'c',
    },
}
respostas_certas=0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das opções abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] : [{rv}]')
    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou')
        respostas_certas+=1
    else:
        print('Você errou')

    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas/qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%')
