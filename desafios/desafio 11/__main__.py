from funcionario import *
from rich import print
from rich.panel import Panel
from rich import inspect

def main():
    fh1 = FuncHorista('João', 12, 200)
    fm1 = FuncMensalista('Pedro', 9500)
    
    fh1.calc_sal()
    fm1.calc_sal()
    
    fh1.analisar_sal()
    print('\n')
    fm1.analisar_sal()
    
    inspect(fh1)


if __name__ == '__main__':
    main()