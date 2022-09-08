"""
Polimorfismo é o principio que permite que cçasses derivadas de uma
mesma superclasse tenha métodos iguais (de mesma assinatura) mas 
comportmanetos diferentes

Mesma assinatura = mesma quantidade e tipo de parâmetros

"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(B):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('Um assunto')
c.fala('outro assunto')