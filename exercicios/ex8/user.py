from rich import print

class Usuario:
    def __init__(self, idade):
        self.idade = idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade_value):
        if idade_value < 0:
            raise ValueError('Idade abaixo de 0, não é permitido')
        self._idade = idade_value
    
    def mudar_idade(self, idade_value):
        self.idade = idade_value