from retangulo import Retangulo

def main():
    r = Retangulo()
    
    try:
        r.base = 1       
        
    except Exception as ex:
        print(ex)
    print(r.medidas)
    
    
if __name__ == '__main__':
    main()