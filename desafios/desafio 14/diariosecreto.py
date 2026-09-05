from rich import print
import pwinput

class DiarioSecreto:
    def __init__(self, senha_diario=None):
        if senha_diario == None:
            senha_diario = self.pede_senha()
            
        self.__segredos = []
        self.__senha = senha_diario
    
    def escrever(self, msg:str):
        self.__segredos.append(msg)
    
    
    def pede_senha(self):
        print('Senha: ', end=' ')
        senha = pwinput.pwinput(prompt='', mask='*')
        return senha

    def valida_senha(self, valor):
        if valor == self.__senha:
            return True
        else:
            raise ValueError('Senha está incorreta!')
    
    def ler(self, senha=None):
        if senha == None:
            senha = self.pede_senha()
            
        validacao = self.valida_senha(senha)
        
        if validacao == True:         
            print('[green]DIARIO LIBERADO![/]')
            for msg in self.__segredos:
                print(f'\tMensagem do diario secreto: {msg}')
        else:
            raise PermissionError('Você não tem permissão! Senha está errada!')
    
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor
