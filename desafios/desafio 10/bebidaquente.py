from abc import ABC, abstractmethod
from time import sleep as sl

class BebidaQuente(ABC):
    def preparar(self):
        print('-' * 5 + 'Inicializando o Preparo' + '-' * 5)
        self.ferver()
        self.misturar()
        self.servir()
        print('----- Bebida Pronta -----')
    
    
    def ferver(self):
        print('1. Fervendo a água a 100 Graus C.')
        
    @abstractmethod
    def misturar(self):
        pass
    
    
    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando a agua fervida, ao pó de café moido!') 
    
    
    def servir(self):
        print('3. Servindo o café em uma xicara!')


class Cha(BebidaQuente):
    def misturar(self):
        print('2. Mergulhando o sache de erva na água fervida!') 
        
        
    def servir(self):
        print('3. Servindo o cha em uma caneca!')
        

class Leite(BebidaQuente):
    def misturar(self):
        print('2. Vaporizando o leite com a água quente!') 
        
        
    def servir(self):
        print('3. Servindo o café em uma xicara!')