class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        
    
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    
    def __add__(self, outro):            
        if self.denominador == outro.denominador:
            novo_n = self.numerador + outro.numerador
            novo_d = self.denominador
        else:
            novo_n = self.numerador * outro.denominador + outro.numerador * self.denominador
            novo_d = self.denominador * outro.denominador
       
        nova_fracao = Fracao(novo_n, novo_d)
        return nova_fracao
           