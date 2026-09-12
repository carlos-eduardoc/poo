from retangulo import Retangulo

def main():
    retangulo_1 = Retangulo(4, 5)
    retangulo_2 = Retangulo(3, 7)
    
    
    print('retangulo 1 é maior que retangulo 2?')
    print(f'R:{retangulo_1 > retangulo_2}'.center(31))
    
    print('retangulo 1 é menor que retangulo 2?')
    print(f'R:{retangulo_1 < retangulo_2}'.center(30))
    

if __name__ == '__main__':
    main()