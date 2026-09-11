class Carteira:
    def __init__(self, saldo=0):
        self._saldo = saldo
        
        
    def __str__(self):
        return f"Saldo na carteira: R${self._saldo:.2f}"
    
    
    def __eq__(self, outra):
        return self._saldo == outra._saldo
    
    
    def __le__(self, outra):
        return self._saldo <= outra._saldo
    
    
    def __iadd__(self, valor):
        self._saldo += valor
        return self
    
    
    def __isub__(self, valor):
        self._saldo -= valor
        return self
    
    
    
# Uso prático
c1 = Carteira(100)
c2 = Carteira(100)

print(c1 == c2) # compara valores bool
# True (compara saldos, não endereços de memória)
c1 += 50
# Adiciona dinheiro via operador
print(c1) # esse é o str mostrando o iadd
# Saldo na carteira: R$150.00
