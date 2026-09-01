# crie uma classe Livro, que permita avançar as paginas, se chegar até a ultima pag
# ele menda um mensagem que ja atingiu um limite de paginas

# plano rapido
 # Usar rich, e o auxiliar (sleep)
  # class Livro, metodo construtor recebe self titulo e quantidade de pags
   # Metodo para avançar paginas, usando for emojis cores, e verificação.
# Detalhe, quando objeto for criado mostra um print sobre o livro.

from auxiliar import line
from rich import print
from time import sleep as sl

class Livro:
    def __init__(self, titulo: str, qntd_pags: int):
        self.titulo = titulo
        self.quantidade_pags = qntd_pags
        self.pag_atual = 1
        print(f':book: [bold blue]Você acabou de abrir [bold white]livro {self.titulo}[/], que [bold white]contem {self.quantidade_pags} paginas[/], você agora se encontra na [bold yellow]pagina {self.pag_atual}[/][/]:book:')
    

    def avancar_pags(self, qntd_avancar=1):
        contador = 0
        for p in range(1, qntd_avancar + 1):
            if self.fim_livro():
                print(f'[blue]Você avançou [bold]{contador}[/] paginas, e agora está na [bold orange1]pagina {self.quantidade_pags}[/] [/]')
                sl(0.30)
                print(f':rotating_light: [red]Você atingiu o limite maximo de paginas no [bold white]livro {self.titulo}[/]![/]:rotating_light:')
                return # break nao pois assim ele nao imprime lá fora 
            else:
                sl(0.2)
                self.pag_atual += 1
                contador += 1
                print(f'[bold white]Pág{self.pag_atual}▶[/]', end=' ')
        print(f'[blue]Você avançou [bold]{contador}[/] paginas, e agora está na [bold orange1]pagina {self.pag_atual}[/] [/]')
    

    def fim_livro(self):
        return True if self.pag_atual == self.quantidade_pags else False
                


l1 = Livro('O Homem mais Rico da Babilonia', 20)
l1.avancar_pags(15)
l1.avancar_pags(100)
l1.avancar_pags(5)

