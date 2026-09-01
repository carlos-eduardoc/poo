from rich import print


class Termostato:
    def __init__(self):
        self.__temperatura = 24
        
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor <= 15 or valor > 30:
            raise ValueError('Temperatura invalida! Minimo é 16 graus e Maximo é 30 graus!')
        if not valor % 1 == 0.5:
            raise ValueError('Temperatura invalida! Seu valor deve terminar inteiro ou com .5!')
        self.__temperatura = valor
    
    @property
    def ftemperatura(self):
        return f'{self.__temperatura}°C'