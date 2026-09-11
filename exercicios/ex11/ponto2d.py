class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __add__(self, outro):
        x_novo = self.x + outro.x
        y_novo = self.y + outro.y
        
        p3 = Ponto2D(x_novo, y_novo)
        return p3
        
        
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y