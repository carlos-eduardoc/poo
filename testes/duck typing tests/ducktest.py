class Pato:
    def __str__(self):
        return f'Animal: {self.__class__.__name__}'
    
    def som(self):
        return 'Quack'


class Cachorro:
    def __str__(self):
        return f'Animal: {self.__class__.__name__}'
    
    def som(self):
        return 'Auau'


class Gato:
    def __str__(self):
        return f'Animal: {self.__class__.__name__}'
    
    def som(self):
        return 'Miauu'

# duck typing aplicado, perceba que todos tem soma, ou seja podemos entao fazer uma forma polimorfica
def fazer_som(obj):
    try:
        print(obj)
        print(obj.som())
    except (AttributeError, TypeError) as ex:
        print(f'{ex}: O objeto {obj} não é capaz de emitir sons')


tipos = [Pato(), Cachorro(), Gato()]
for tipo in tipos:
    fazer_som(tipo)