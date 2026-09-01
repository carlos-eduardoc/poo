from diariosecreto import DiarioSecreto


def main():
    d1 = DiarioSecreto()
    d1.escrever('OI a senha é linux é melhor que windows')
    d1.escrever('Eu gosto de fulano')
    print(d1.ler('linux é melhor que windows'))
    

if __name__ == '__main__':
    main()