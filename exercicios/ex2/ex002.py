class Ganfanhoto:
    """
    Esta classe gera um Gafanhoto, que é uma pessoa que contém nome e idade
    Para criar uma nova pessoa:
    variavel = Gafanhoto(nome, idade)
    -----------------------------------------------------------------------
    Metodos:
    aniversario() e mensagem()
    aniversario() - Ele quando chamado ele aumenta 1, na idade do Gafanhoto
    mensagem() - Retorna uma mensagem personalizada

    """

    def __init__(self, nome='', idade=0): # metodo construtor
        # ATRIBUTOS DE INSTANCIA
        self.nome = nome
        self.idade = idade


    # METODOS DE INSTANCIA
    def aniversario(self):
        self.idade += 1
     
    
    def __str__(self):
        return f'{self.nome} é Ganfanhoto(a), e tem {self.idade} anos de idade!'


# Declaração do objeto
g1 = Ganfanhoto('Maria Benedita', 55)
g2 = Ganfanhoto('Joao Pedro', 9)

g1.aniversario()
g2.aniversario()

print(g1)
print('-' * 60)
print(g2)

# mostra a doc da class, print(g1.__doc__) # dunder attribute