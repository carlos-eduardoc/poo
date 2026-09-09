from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
        
    def saque(self, valor):
        validacao = self.validador_saque(valor)
        if validacao:
            self._saldo -= valor
            print(f'Saque realizado! -R${valor:,.2f} ')