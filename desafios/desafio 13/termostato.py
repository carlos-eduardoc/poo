from rich import print


class Termostato:
    def __init__(self):
        self.__temperatura = 24
        
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError('Temperatura invalida! Seu valor deve terminar inteiro ou com .5!')
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor
        
    @property
    def ftemperatura(self):
        return f'{self.__temperatura}°C'