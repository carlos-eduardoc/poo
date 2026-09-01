from rich import print
from rich.panel import Panel

class ContaBancaria:
    def __init__(self, titular:str, saldo:float, limite:float):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def __str__(self):
        return f'O titular da conta é {self.titular}, tem {self.formatacao(self.saldo)}, e um limite de {self.formatacao(self.limite)}'
    

    def __eq__(self, outra_conta):
        if not isinstance(outra_conta, ContaBancaria):
            return NotImplemented
        else:
            return self.titular == outra_conta.titular and self.saldo == outra_conta.saldo and self.limite == outra_conta.limite

    def formatacao(self, valor):
        return f'R${valor:,.2f}'
    

    def depositar(self, valor):
        dep = Panel('[bold white]Deposite seu dinheiro[/]'.center(60), width=50, style='bold black')
        print(dep)

        self.saldo += valor
        result = f'[bold white]Deposito autorizado | Titular: {self.titular} | Valor: {self.formatacao(valor)} | Saldo A: {self.formatacao(self.saldo)}[/]'
        dep_result = Panel(result, width=50, style='bold black', title='[bold white]Deposito autorizado[/]')

        return dep_result


    def sacar(self, valor):
        result_negado = f'[bold red]Saque negado! :rotating_light:'
        dep = Panel('[bold white]Saque seu dinheiro[/]'.center(60), width=50, style='bold black')
        print(dep)

        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            result = f'[bold white]Saque autorizado | Titular: {self.titular} | Valor: {self.formatacao(valor)} | Saldo A: {self.formatacao(self.saldo)}[/]'

            saq_result = Panel(result, width=50, style='bold black', title='[bold white]Saque autorizado[/]')
            return saq_result
        else:
            saq_result_negado = Panel(result_negado, width=50, style='bold black', title='[bold white]Saque negado[/]')
            return saq_result_negado
        

    def transferir(self, valor, destino):
        if valor > self.saldo + self.limite:
            return f'[red]Transferencia cancelada![/]'
        else:
            self.saldo -= valor
            destino.saldo += valor
            return f'[green]Transferencia para {destino.titular} foi concluida![/]'


c1 = ContaBancaria('Carlos Eduardo', 2500, 5500)
c2 = ContaBancaria('Carlos Pedro', 2500, 5500)

print(c1.depositar(500))
print(c1.sacar(500))
print(c1.transferir(500, c2))
print(c1)
print(c2)