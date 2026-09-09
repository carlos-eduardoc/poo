from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, saldo):
        super().__init__()
        self._saldo = saldo
        
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Não é permitido alterar seu saldo!')
    
    
    @abstractmethod
    def saque(self, valor):
        pass
    
    def validador_saque(self, valor):
        if valor > self._saldo:
            raise ValueError('Não foi possivel realizar o saque, valor é maior que seu saldo!')
        elif valor < 1:
            raise ValueError('Não foi possivel realizar o saque, o valor é menor que R$1,00')
        else:
            return True