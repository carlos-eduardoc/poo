from abc import ABC, abstractmethod
from conta import Conta
from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente
from rich import inspect

def main():
    contap = ContaPoupanca(2000)
    try:
        contap.saque(2000)
    except Exception as ex:
        print(ex)
        
    print(contap.saldo)
    inspect(contap, private=True, methods=True)
    
    contac = ContaCorrente(2000)
    try:
        contac.saque(2000)
    except Exception as ex:
        print(ex)
        
    print(contap.saldo)
    inspect(contac, private=True, methods=True)

if __name__ == '__main__':
    main()