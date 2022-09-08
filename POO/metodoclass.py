from random import randint

class Pessoa:
    ano_atual = 2021
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    def ano_nasc(self):
        print(self.ano_atual-self.idade)
    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual-ano_nasc
        return cls(nome, idade)
    @staticmethod
    def gera_id():
        rad = randint(0,30)
        return rad
p1 = Pessoa('Julia', 18)
ano = Pessoa.por_ano_nasc('JULIA', 2003)
print(Pessoa.por_ano_nasc)
print(p1.nome, p1.idade)
p1.ano_nasc()
print(Pessoa.gera_id()) # pode ser chamado tanto pela classe
print(p1.gera_id()) # como pela instância

