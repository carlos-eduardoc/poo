from diariosecreto import DiarioSecreto


def main():
    d1 = DiarioSecreto()
    d1.escrever('OI a senha nao é linux é melhor que windows')
    d1.escrever('Eu gosto de fulano')
    print(d1.ler())
    

if __name__ == '__main__':
    main()