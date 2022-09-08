class Produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco
    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco*(porcentagem/100))
    # Getters
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco=valor
p1 = Produto('nome', 50)
p1.desconto(10)
p2 = Produto('nome 2', 15)
p2.desconto(10)
print(p1.preco, p2.preco)
