class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        area = self.largura * self.altura
        return area
    
    
    def __lt__(self, outro):
        return self.area() < outro.area()

    
    def __gt__(self, outro):
        return self.area() > outro.area()