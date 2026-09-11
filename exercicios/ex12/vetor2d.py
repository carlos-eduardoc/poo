class Vetor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __add__(self, outro):
        novo_x = self.x + outro.x
        novo_y = self.y + outro.y
        vetor_novo = Vetor2D(novo_x, novo_y)
        return vetor_novo
    
    
    def __sub__(self, outro):
        novo_x = self.x - outro.x
        novo_y = self.y - outro.y
        vetor_novo = Vetor2D(novo_x, novo_y)
        return vetor_novo
    
    
    def __mul__(self, valor):
        novo_x = self.x * valor
        novo_y = self.y * valor
        vetor_novo = Vetor2D(novo_x, novo_y)
        return vetor_novo