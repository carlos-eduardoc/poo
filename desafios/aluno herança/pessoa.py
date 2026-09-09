from abc import ABC, abstractmethod
import datetime
class Pessoa(ABC):
    ano = datetime.datetime.today().year
    
    def __init__(self, nome:str, nascimento:int=1940):
        super().__init__()
        self._nome = nome
        self._nascimento = nascimento
        
        
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, valor):
        if valor > Pessoa.ano or valor < 1940:
            raise ValueError('Ano Invalido!')
        self._nascimento = valor
    
    
    @property
    def idade(self):
        return Pessoa.ano - self._nascimento
    
    @idade.setter
    def idade(self, valor):
        raise ValueError(f'Não é possivel alterar a idade de {self._nome}, altere o ano de nascimento!')
