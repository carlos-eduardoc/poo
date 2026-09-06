class Retangulo:
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        self._area = None
    
    
    @property
    def base(self):
        return f'A Base do Retangulo tem {self._base} centimetros'
    
    @base.setter
    def base(self, valor):
        if valor < 1:
            raise ValueError('Não é permitido valores menores que 1')
        self._base = valor    
    
    @property
    def altura(self):
        return f'A altura do Retangulo tem {self._altura} centrimetros'
    
    @altura.setter
    def altura(self, valor):
        if valor < 1:
            raise ValueError('Não é permitido valores menores que 1')
        self._altura = valor    
    
    
    @property
    def medidas(self):
        return f'Base: {self._base} \nAltura: {self._altura} \nArea: {self._base * self._altura}'
    
    @medidas.setter
    def medidas(self, valores:tuple):
        if len(valores) > 2:
            raise ValueError('Digite apenas 2 itens!')
        
        self._base = valores[0]
        self._altura = valores[1]
        
    
    @property
    def area(self):
        return self._base * self._altura

    @area.setter
    def area(self, valor):
        raise PermissionError(f'Voce não tem permissao para alterar este Dado!')
        