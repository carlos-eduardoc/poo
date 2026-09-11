from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod
    def analisador(self, valor):
        print(f'Tipo desconhecido: {type(valor)}')
    
    @analisador.register(str)
    def _(self, valor):
        print('Valor é uma cadeia de caracteres')
    
    @analisador.register(int)
    def _(self, valor):
        print('Valor é numero inteiro')
    
    @analisador.register(tuple)
    def _(self, valor):
        print('Valor é uma coleção de dados')
    
    @analisador.register(list)
    def _(self, valor):
        print('Valor é uma coleção de dados')
    
    @analisador.register(float)
    def _(self, valor):
        print('Valor é um numero de ponto flutuante')
    
    @analisador.register(tuple)
    def _(self, valor):
        print('Valor é uma coleção de dados')
    
    @analisador.register(bool)
    def _(self, valor):
        print('Valor é do tipo verdadeiro ou falso')

analisar = Analisador()
analisar.analisador(False)