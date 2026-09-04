from termostato import Termostato
from rich import print

def main():
    t = Termostato()
    
    try:
        t.temperatura = 16
        print(f'Sucesso! {t.ftemperatura}') 
    except ValueError as ex:
        print(f'Erro capturado! {ex}')   

if __name__ == "__main__":
    main()