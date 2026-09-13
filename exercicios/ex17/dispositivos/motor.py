class Motor: 
    def __init__(self):
        self.status = False
    def ligar(self):
        self.status = True
        return 'ligando o motor...'
        
    def __str__(self):
        return f'Status do motor: {self.status}'