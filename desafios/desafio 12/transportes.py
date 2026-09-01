from abc import ABC, abstractmethod
from rich import print
from rich.table import Table

table = Table(title='Calculo de Frete')

class Transporte(ABC):
    def __init__(self, dist):
        self.distancia = dist
        self.frete = 0
    
    
    @abstractmethod
    def calcular_frete(self):
        pass
    
    
class Moto(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 0.50
    
    
    def calcular_frete(self):
        self.frete = self.fator * self.distancia
        
    
class Caminhao(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 1.28
    
    
    def calcular_frete(self):
        if self.distancia < 50:
            print('O raio minimo é de 50km!')
            return
        self.frete = self.fator * self.distancia
    
    
class Drone(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 9.50
        
        
    def calcular_frete(self):
        if self.distancia > 10:
            print('O raio maximo é de 10km!')
            return
        self.frete = self.fator * self.distancia
    