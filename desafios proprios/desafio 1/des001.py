from rich import print

class Retangulo:
    def __init__(self, altura, largura):
        self.alt = altura
        self.larg = largura
        print(f'[bold white]O Retangulo foi criado com sucesso! Contém [bold orange1]{self.alt} cm de altura e {self.larg} cm de largura[/][/]')


    def __str__(self):
        return f'Retangulo -> {self.alt} x {self.larg}'
    

    def calc_per(self):
        calculo_p = 2 * (self.alt + self.larg)
        return f'[bold white]O perimetro deste Retangulo é de {calculo_p:.1f}[/]'

    

    def calc_area(self):
        calculo_a = self.alt * self.larg
        return f'[bold white]A area deste Retangulo é de {calculo_a:.2f}[/]'




r1 = Retangulo(25, 25)
print(r1.calc_per())
print(r1.calc_area())