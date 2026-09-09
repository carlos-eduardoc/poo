from diariosecreto import DiarioSecreto


def main():
    print('Digite a senha')
    d1 = DiarioSecreto()
    d1.escrever('OI a senha nao é linux é melhor que windows')
    d1.escrever('Eu gosto de fulano')
    
    try:
        print('Altere a senha')
        d1.senha = '123carlos'
        print('Senha alterada!')
    except Exception as ex:
        print(ex)
    
    try:
        print(d1.ler())
    except Exception as ex:
        print(ex)
    

if __name__ == '__main__':
    main()