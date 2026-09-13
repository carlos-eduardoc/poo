class Radio: 
    def __init__(self):
        self.status = False
        
    def ligar(self):
        self.status = True
        return 'ligando o radio...'
        
    def __str__(self):
        return f'Status do radio: {self.status}'