""" 
Crie uma classe Personagem.

Requisitos:

Nome público.
Vida privada (__vida).
Vida inicial = 100.

Métodos:

receber_dano(valor)
mostrar_vida()
"""

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100
        self.vida_inicial = 100
    
    
    def receber_dano(self, valor):
        if self.__vida == 0:
            return 'Tu ta morto kkkk'
        
        if valor < 0:
            return 'Desta vez tu escapou'

        if valor > 0:
            if valor >= self.__vida:
                self.__vida = 0
                return 'Recebeu dano e morreu kkk'
            self.__vida -= valor
            return 'Recebeu dano kkk!'
    
    
    def mostrar_vida(self):
        return f'Vida: {self.__vida}'
    
    
personagem = Personagem('Felijão')
print(personagem.receber_dano(10))

print(personagem.mostrar_vida())
print(personagem.receber_dano(100))
print(personagem.mostrar_vida())
print(personagem.receber_dano(10))

