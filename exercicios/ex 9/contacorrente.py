from conta import Conta


class ContaCorrente(Conta):
    taxa_fixa = 2
    
    def __init__(self, saldo):
        super().__init__(saldo)
    
    def saque(self, valor):
        validacao = self.validador_saque(valor)
        if validacao:
            saldo_apos_contas = self._saldo - ContaCorrente.taxa_fixa - valor 
            if saldo_apos_contas > 0:  
                self._saldo -= ContaCorrente.taxa_fixa
                self._saldo -= valor
                print(f'Saque realizado! -{valor + ContaCorrente.taxa_fixa:,.2f}')
            else:
                raise ValueError('Saldo invalido para o saque!')