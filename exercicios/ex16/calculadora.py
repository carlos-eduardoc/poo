from functools import singledispatchmethod

class Calculadora:
    @singledispatchmethod
    def dobrar(self, valor):
        return f'Valor desconhecido: {valor}'
    
    