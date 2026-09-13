from ducktyping import ativar_dispositivo
from motor import Motor
from lampada import Lampada
from radio import Radio


def main():
    objetos = [Motor(), Lampada(), Radio(), 'oi']
    for obj in objetos:
        ativar_dispositivo(obj)
    

if __name__ == '__main__':
    main()