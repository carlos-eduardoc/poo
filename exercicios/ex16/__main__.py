from calculadora import Calculadora

def main():
    c1 = Calculadora()
    
    print('Dobrar: INT'.center(20))
    print('-' * 20)  
    print(f'{c1.dobrar(10)}'.center(17))
    
    print('\n')
    
    print('Dobrar: FLOAT'.center(20))
    print('-' * 20)  
    print(f'{c1.dobrar(2.5)}'.center(20))
    
    print('\n')
    
    print('Dobrar: STR'.center(20))
    print('-' * 20)  
    print(c1.dobrar('pooEMpython').center(20))
    
    print('\n')
    
    print('Dobrar: LIST'.center(20))
    print('-' * 20)  
    print(f'{c1.dobrar([1, 2, 3])}'.center(20))
    
    
if __name__ == '__main__':
    main()