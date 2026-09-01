# crie ma classe produto, ela cadastra nome e preço, no final um metodo de etiqueta.

from rich.panel import Panel
from rich import print
from auxiliar import line

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        preco_formatada = f'R${self.preco:,.2f}'
        conteudo_etiq = f'[bold white]{(self.nome).center(40)}[/] \n[white]{"-" * 40}[/] \n[bold green]{preco_formatada.center(40, '.')}[/]'
        etiq = Panel(conteudo_etiq, 
            title=' [ Produto ]', 
            width=45, 
            style='bold yellow'
            
                    )
        
        return etiq


p1 = Produto('Iphone 17 Pro Max', 8_000)
p2 = Produto('Fone Gamer', 850)

print(p1.etiqueta())
line(45)
print(p2.etiqueta())