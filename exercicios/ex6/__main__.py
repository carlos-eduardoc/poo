from avaliacao import *
from rich import print, inspect


def main():
    av1 = Avaliacao('Carlos', 'Matematica')
    av1.set_nota(-55) # usando o setter
    print(av1.get_nota())
    inspect(av1, private=True)
    


if __name__ == '__main__':
    main()