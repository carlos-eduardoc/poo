from ponto2d import Ponto2D

def main():
    pontos1 = Ponto2D(4, 4)
    pontos2 = Ponto2D(4, 6)
    
    p3 = pontos1 + pontos2
    print(f'X: {p3.x}')
    print(f'Y: {p3.y}')
    
    print(pontos1 == pontos2)

if __name__ == '__main__':
    main()