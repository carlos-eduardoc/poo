from conta import Conta


class ContaCorrente(Conta):
    taxa_fixa = 2
    
    def __init__(self, saldo):
        super().__init__(saldo)
    
    def saque(self, valor):
        validacao = self.validador_saque(valor)
        if validacao == True:
            self._saldo -= valor
            self._saldo -= ContaCorrente.taxa_fixa