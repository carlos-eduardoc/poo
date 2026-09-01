# Declaração da class
class Ganfanhoto:
    def __init__(self): # metodo construtor
        # ATRIBUTOS DE INSTANCIA
        self.nome = ''
        self.idade = 0


    # METODOS DE INSTANCIA
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return f'{self.nome} é Ganfanhoto(a), e tem {self.idade} anos de idade!'


# Declaração do objeto
g1 = Ganfanhoto()
g2 = Ganfanhoto()

g1.nome = 'Maria Benedita'
g1.idade = 55
g1.aniversario()

g2.nome = 'Joao Pedro Todo Cagado'
g2.idade = 9

for a in range(5):
    g2.aniversario

print(g1.mensagem())
print('-' * 60)
print(g2.mensagem())