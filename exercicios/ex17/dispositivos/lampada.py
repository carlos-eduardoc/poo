class Lampada: 
    def __init__(self):
        self.status = False
        
    def ligar(self):
        self.status = True
        return 'ligando a lampada...'
        
    def __str__(self):
        return f'Status da lampada: {self.status}'