from formatador import Formatador

def main():
    f1 = Formatador()
    
    print('Formatação INT'.center(30))
    print('-' * 30)
    print(f1.formatar(1000).center(30))
    
    print('\n')
    
    print('Formatação STR'.center(30))
    print('-' * 30)
    print(f1.formatar('oi me segue no github e de uma estrela:)').center(20))
    
    print('\n')
        
    print('Formatação LIST'.center(30))
    print('-' * 30)
    print(f1.formatar([1, 'oi', 99, 2.9]).center(30))
    
    print('\n')
        
    print('Formatação DESCONHECIDA'.center(30))
    print('-' * 30)
    print(f1.formatar(2.9).center(30))
        
        
    
if __name__ == '__main__':
    main()