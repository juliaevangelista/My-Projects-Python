#        Índices
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de roma'  # iterável
tamanho_frase = len(frase)
contador = 0
nova_string =''
input_do_usuario = input('Qual letra você deseja deixar maiúsculo: ')

# iteração/interar
while contador< tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
      nova_string += input_do_usuario.upper()
    else:
      nova_string += letra
    contador+=1
    
print(nova_string)