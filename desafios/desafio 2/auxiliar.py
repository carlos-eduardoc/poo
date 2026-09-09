from rich import print

cores = [
    31, # vermelho# 0
    32, # verde # 1
    33, # 2 # amarelo
    34, # azul # 3
    35, # 4 rosa
    36, # azul # 5
    37, # branco ou cinza # 6
    30 # preto # 7
]

def cor(indice, msg):
    print(f'\033[{cores[indice]}m{msg}\033[0m')
    return


def line(tamanho=75):
    print(f'[bold green]{'-' * tamanho}[/]')
    return
