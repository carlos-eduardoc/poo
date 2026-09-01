# Rich com traceback, ele mostra o erro de forma mais visual e bonita.
# usa from rich.traceback importal install
# para uso usamos install(), assim que acontecer um erro ele reporta ele de uma maneira mais elegante

from rich.traceback import install
from rich import inspect
install()

def divisao(x, y):
    return x / y

print(divisao(50, 2))


inspect(divisao)