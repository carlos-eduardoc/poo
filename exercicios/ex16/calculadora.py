from functools import singledispatchmethod

class Calculadora:
    @singledispatchmethod
    def dobrar(self, valor):
        return f'Valor desconhecido: {valor}'
    
    @dobrar.register(int)
    def _(self, valor):
        return valor * 2
    
    @dobrar.register(float)
    def _(self, valor):
        return valor * 2
    
    @dobrar.register(str)
    def _(self, valor):
        return valor * 2
    
    @dobrar.register(list)
    def _(self, valor):
        return valor * 2