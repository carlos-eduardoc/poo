from poligno import *

def main():
    q1 = Quadrado(4, 20)
    c1 = Circulo(20)
    
    print(f'Perimetro do quadrado = {q1.perimetro()}cm')
    print(f'Area do quadrado = {q1.area()}m²')
    
    print(f'Perimetro do circulo = {c1.perimetro():.1f}cm')
    print(f'Area do circulo = {c1.area():.1f}m²')



if __name__ == "__main__":
    main()