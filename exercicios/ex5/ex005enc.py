""" 
com:

__saldo privado
_titular protegido
métodos para controlar alterações do saldo

Requisitos:

depositar(valor)
sacar(valor)
mostrar_saldo()

Regras:

Não permitir depósito negativo.
Não permitir saque negativo.
Não permitir sacar mais dinheiro do que existe na conta.
O saldo deve ser alterado apenas pelos métodos da classe.
"""

class ContaBancaria:
    def __init__(self, titular):
        self._titular = titular
        self.__saldo = 0
        
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return 'Sucesso'
        return 'Retrocesso'
    
    
    def sacar(self, valor):
        if self.__saldo < valor:
            return f'{self._titular} oce tem {self.__saldo} não {valor}'
        if valor > 0:
            self.__saldo -= valor
            return f'{self._titular} tu sacou {valor}'
        else:
            return 'Num pode sacar valor negativo abestado'
    
    def mostrar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria("Carlos")

print(conta.mostrar_saldo())

conta.depositar(500)
print(conta.mostrar_saldo())

conta.sacar(200)
print(conta.mostrar_saldo())

conta.depositar(-100)
print(conta.mostrar_saldo())