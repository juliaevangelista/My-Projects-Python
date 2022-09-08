clientes = {
    'cliente1': {
        'nome':'Julia',
        'sobrenome':'Ferreira'
    },
    'cliente2': {
        'nome':'João',
        'sobrenome':'Silva'
    },
    'cliente3': {
        'nome':'Maria',
        'sobrenome':'Moreira'
    },
}
for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')