from user import *

def main():
    user1 = Usuario(12)
    print(user1.idade)
    
    try:
        user1.mudar_idade(-17)
    except:
        print('Erro capturado!')
    
    try:
        user1.mudar_idade(17)
    except:
        print('Erro capturado!')
    
    print(user1.idade)
    
    
if __name__ == '__main__':
    main()