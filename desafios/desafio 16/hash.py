from hashlib import sha256


class Hash:
    def __init__(self, chave=None):
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
    
    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self, valor):
        if len(valor) > 0:
            self.__hash = sha256(valor.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Sua senha tem menos de 1 caracter!')
    
    def validar(self, chave):
        senha = sha256(chave.encode('utf-8')).hexdigest()
        if senha == self.__hash:
            print('Senha é valida!')
        else:
            raise ValueError('Senha não é valida!')