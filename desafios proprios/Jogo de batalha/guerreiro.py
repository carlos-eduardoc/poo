from superclasse import Personagem
from rich.panel import Panel
 
LARGURA_PAINEL = 90


class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque=25, defesa=40, energia=100):
        super().__init__(nome, vida, ataque, defesa, energia)
        self.armas_guerreiro = ['lança', 'espada']
        self.ativada_arma = False
        self.ativada_armadura = False


    def ativar_arma(self, arma:str):
        if arma.lower().strip() in self.armas_guerreiro:
            if not self.ativada_arma:
                self.ataque += 5

                conteudo = Panel(
                    f'(...) [bold white]{self.__class__.__name__} {self.nome} ativou a [bright_yellow]{arma} do guerreiro[/], [yellow on green]ganho de +5 ataque[/][/]!',
                    title='[bold green]Arma ativada[/]',
                    width=LARGURA_PAINEL,
                    border_style='green'
                )
                self.ativada_arma = True
                return conteudo
            
        else:
            conteudo = Panel(
                f'[bold white]A arma [bright_yellow]{arma}[/] não está na lista de armas do [orange1]guerreiro[/]!',
                title='[bold red]Arma indisponível[/]',
                width=LARGURA_PAINEL,
                border_style='red'
                )
            return conteudo
        

    def ativar_desativar_armadura(self):
        self.ativada_armadura = not self.ativada_armadura

        if self.ativada_armadura:
            self.defesa += 25
            return Panel(
                f'[bold white]A [bright_yellow]armadura do guerreiro[/] foi ativada no [cyan]{self.__class__.__name__} {self.nome}[/].',
                title='[bold bright_yellow]Armadura ativada[/]',
                width=LARGURA_PAINEL,
                border_style='bright_yellow'
            )
        else:
            self.defesa -= 25
            return Panel(
                f'[bold white]A [red]armadura do guerreiro[/] foi desativada no [cyan]{self.__class__.__name__} {self.nome}[/].',
                title='[bold red]Armadura desativada[/]',
                width=LARGURA_PAINEL,
                border_style='red'
            )