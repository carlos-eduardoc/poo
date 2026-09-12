from functools import singledispatchmethod

class Formatador:
    @singledispatchmethod
    def formatar(self, valor):
        return f'Valor desconhecido: {valor}'
    
    
    @formatar.register(int)
    def _(self, valor):
        return f'{valor:,.2f}'.replace(',', '.')

    
    @formatar.register(str)
    def _(self, valor):
        return f'{valor.upper()}'
    
    
    @formatar.register(list)
    def _(self, valor):
        return f'Lista com {len(valor)} itens'