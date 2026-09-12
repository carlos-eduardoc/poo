from functools import singledispatchmethod

class Formatador:
    @singledispatchmethod
    def formatar(self, valor):
        return f'Tipo desconhecido: {valor}'
    
    @formatar.register(int)
    def _(self, valor):
        return f''

    
    @formatar.register(str)
    def _(self, valor):
        return f''
    
    
    @formatar.register(list)
    def _(self, valor):
        return f''