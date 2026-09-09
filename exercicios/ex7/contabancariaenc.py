"""Crie uma classe ContaBancaria com o atributo protegido _saldo. 
Implemente uma @property para o saldo que permita apenas leitura. Para alterar o saldo, 
implemente um método depositar(valor) que lance um ValueError caso o depósito seja negativo."""

from rich import print

class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Deposite apenas valores positivos acima de 1 real!')
        self._saldo += valor
        