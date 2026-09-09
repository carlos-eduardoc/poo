from transportes import *
from rich.table import Table

def main():
    transportes = [Moto(5), Caminhao(51), Drone(8)]
    
    table.add_column("Veiculo", justify='center', style='white')
    table.add_column('Distancia', justify='center', style='white')
    table.add_column('Fator', justify='center', style='white')
    table.add_column('Frete Total', justify='center', style='white')
    #
    
    for t in transportes:
        t.calcular_frete()
        table.add_row(f'{t.__class__.__name__}', f'{t.distancia}km', f'{t.fator}', f'R${t.frete:.2f}')
    print(table)


if __name__ == "__main__":
    main()