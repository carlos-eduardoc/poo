from rich import print
from contabancariaenc import *


def main():
    conta1 = ContaBancaria(1500)
    print(conta1.saldo)
    
    conta1.depositar(-1500)
    print(conta1.saldo)
    
if __name__ == "__main__":
    main()