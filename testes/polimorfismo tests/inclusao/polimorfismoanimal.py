from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
        
    @abstractmethod
    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Au Au!"
    
class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Miau!"
    
class Pato(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Quack!"
   
        
# Uso Polimórfico
animais = [Cachorro("Bandit"), Gato("Frajola"), Pato("Donald")]
for animal in animais:
    print(animal.emitir_som())