from termostato import Termostato
from rich import print

def main():
    t = Termostato()
    
    try:
        t.temperatura = 16
    except ValueError as ex:
        print(f'Erro capturado! {ex}')   
        
    print(f'Temperatura atual é de {t.ftemperatura}') 


if __name__ == "__main__":
    main()