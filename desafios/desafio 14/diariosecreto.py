from rich import print


class DiarioSecreto:
    def __init__(self):
        self.__segredos = []
        self.__senha = "linux é melhor que windows"
    
    def escrever(self, msg:str):
        self.__segredos.append(msg)
    
    def ler(self, senha):
        if senha == self.__senha:
            print('[green]DIARIO LIBERADO![/]')
            for msg in self.__segredos:
                print(f'\tMensagem do diario secreto: {msg}')
        else:
            raise PermissionError('Você não tem permissão! Senha está errada!')