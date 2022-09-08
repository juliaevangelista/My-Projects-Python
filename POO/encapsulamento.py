"""
public, protected, private
_ privado (public _)
__ privado (_NOMECLASSE__nomeatributo)
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def lista_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    def apagar_cliente(self):
        del self.__dados['clientes'][id]
bd = BaseDeDados()
bd.inserir_clientes(1,'Julia')
bd.lista_cliente()

