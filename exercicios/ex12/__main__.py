from vetor2d import Vetor2D

def main():
    v1 = Vetor2D(5, 4)
    v2 = Vetor2D(6, 7)
    v3_soma = v1 + v2
    
    print('soma'.center(8))
    print(f'X: {v3_soma.x}'.center(10))
    print(f'Y: {v3_soma.y}'.center(10))
    print('-' * 10)
    
    print('subtração'.center(10))
    v3_subt = v1 - v2
    print(f'X: {v3_subt.x}'.center(10))
    print(f'Y: {v3_subt.y}'.center(10))
    print('-' * 10)
    
    print('multiplicação'.center(10))
    v3_mult = v1 * 3
    print(f'X: {v3_mult.x}'.center(10))
    print(f'Y: {v3_mult.y}'.center(10))
    print('-' * 10)


if __name__ == '__main__':
    main()
    