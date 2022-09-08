from classesescritor import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Julia')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
