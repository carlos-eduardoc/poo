# Contexto: Crie um sistema de conta bancaria simples: contendo atributos:
# numumero da conta, nome do tiitular, saldo, com os methodos:
# sacar e depositar
from auxiliar import cor
tamanho = 120

class ContaBancaria:
    def __init__(self, id: int, titular: str, saldo: float):
        self.id = id
        self.titular = titular 
        self.saldo = saldo
        cor(1, f'Conta criada com sucesso | ID: {self.id} | Titular: {self.titular} | Saldo: R${self.saldo:,.2f}')


    def sacar(self, valor):
        cor(7, 'Saque seu dinheiro'.center(tamanho))
        cor(2, '-' * tamanho)
            
        if valor > self.saldo:
            print(f'Limite excedido! O valor de {valor:,.2f}, esta acima de seu saldo atual de R${self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'\033[32mSaque Autorizado | Informações | ID: {self.id} | Titular: {self.titular} | Quantidade: {valor:,.2f} | Saldo A: {self.saldo:,.2f}\033[0m')


    def depositar(self, valor):
        cor(7, 'Deposite seu dinheiro'.center(tamanho))
        cor(2, '-' * tamanho)
        
        self.saldo += valor
        print(f'\033[32mDeposito Autorizado | Informações | ID: {self.id} | Titular: {self.titular} | Quantidade: {valor:,.2f} | Saldo A: {self.saldo:,.2f}\033[0m')

    
    def __str__(self):
        return f'ID: {self.id} | Titular: {self.titular} | Saldo: {self.saldo}'


p1 = ContaBancaria(12345, 'Carlos Eme', 2430)
cor(2, '-' * tamanho)
p1.depositar(567)
cor(2, '-' * tamanho)
p1.sacar(2500)

cor(3, '=' * tamanho)


print(p1)



