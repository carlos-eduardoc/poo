from retangulo import Retangulo

def main():
    r = Retangulo(1, 3)
    print('METODO INICIADOR')
    print(r.medidas)
    
    print('METODOS BASE A ALTURA')
    try:
        r.base = 6
        r.altura = 7
    except Exception as ex:
            print(ex)
    print(r.medidas)
    
    print('METODO MEDIDAS')
    try:
        r.medidas = (4, 9)
    except Exception as ex:
        print(ex)
        
    print(r.medidas)
    
    
if __name__ == '__main__':
    main()