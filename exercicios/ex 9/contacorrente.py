from conta import Conta


class ContaCorrente(Conta):
    taxa_fixa = 2
    
    def __init__(self, saldo):
        super().__init__(saldo)
    
    
    def validador_saque(self, valor):
        saldo_apos_contas = self._saldo - ContaCorrente.taxa_fixa - valor
        if valor < 1:
            raise ValueError('Não foi possivel realizar o saque, o valor é menor que R$1,00')
        elif saldo_apos_contas <= 0:
            raise ValueError('Não foi possivel realizar o saque, valor + taxa é menor ou igual que R$0.00!')
        else:
            return True
    
    
    def saque(self, valor):
        validacao = self.validador_saque(valor)
        if validacao:
            self._saldo -= ContaCorrente.taxa_fixa
            self._saldo -= valor
            print(f'Saque realizado! -R${valor + ContaCorrente.taxa_fixa:,.2f}')