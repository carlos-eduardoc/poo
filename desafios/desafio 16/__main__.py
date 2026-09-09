from hash import Hash

def main():
    h = Hash('Outra senha')
    print(h.senha)
    h.senha = 'linuxémuitomelhorquewindows'
    print(h.senha)
    
    h.validar('linuxémuitomelhorquewindows')
    

if __name__ == '__main__':
    main()