""" 
Crie uma classe Cofre.

Requisitos:

O saldo do cofre deve ser privado (__saldo).
O saldo inicial deve ser 0.
Criar um método depositar(valor).
Criar um método mostrar_saldo().
Não permitir depósitos negativos.
"""

class Cofre:
    def __init__(self):
        self.__saldo = 0
    
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return 'Sucesso'
        return 'Retrocesso'
    
    def mostrar_saldo(self):
        return self.__saldo


cofre = Cofre()

print(cofre.depositar(1200))
print(cofre.mostrar_saldo())