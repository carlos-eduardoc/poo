from abc import ABC, abstractmethod

class Poligno(ABC):
    def __init__(self, qntd_lados):
        self.q_lados = qntd_lados
        
        
    @abstractmethod
    def area(self):
        pass
    
    
    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(Poligno):
    def __init__(self, qntd_lados, lado):
        super().__init__(qntd_lados)
        self.lados = lado
    
    def perimetro(self):
        calculo = self.lados * self.q_lados
        return calculo
    
    def area(self):
        calculo = self.lados ** 2
        return calculo
    

class Circulo(Poligno):
    def __init__(self, raio):
        self.raio = raio
        
    def perimetro(self):
        calculo = (self.raio * 2) * 3.14
        return calculo
    
    def area(self):
        calculo = (self.raio ** 2) * 3.14
        return calculo