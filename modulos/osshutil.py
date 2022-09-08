import os
import shutil

caminho_original = r'C:\a\pasta1'
caminho_novo = r'C:\a\pasta2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        ant_arquivo = os.path.join(raiz, arquivo)
        novo_arquivo = os.path.join(caminho_novo, arquivo)

        if '.txt' in arquivo:
            shutil.copy(ant_arquivo, novo_arquivo)
            print(f'Arquivo {arquivo} movido com sucesso')

