from servicos.ducktyping import ativar_dispositivo
from dispositivos import motor, lampada, radio

def main():
    objetos = [motor.Motor(), lampada.Lampada(), radio.Radio(), 'oi']
    for obj in objetos:
        ativar_dispositivo(obj)
    

if __name__ == '__main__':
    main()