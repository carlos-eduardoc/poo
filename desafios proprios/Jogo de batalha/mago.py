from superclasse import Personagem
from rich.panel import Panel
from rich.live import Live

# declara class, metodo construtor, coloca as caracteristicas de Personagem
# chama super().__init__(....) adiciona os atributos do mago.

# metodos lancar fogo e curar ele mesmo
#lancar fogo ele vai ser um novo tipo de ataque só que evoluido e sem combate
# curar ele depende de status se tiver do tempo de ele usar ele pode usar e se curar

# é isso ae
largura = 90

class Mago(Personagem):
    def __init__(self, nome, vida=55, ataque=25, defesa=15, energia=100):
        super().__init__(nome, vida, ataque, defesa, energia)
        self.ataque_fogo = 35
        self.vida_inicial = vida


    def lancar_fogo(self, alvo):
        return self.executar_ataque(alvo, self.ataque_fogo, 10)
            

    def curar(self, quantidade):
        conteudo = []
        mensagem_negacao = f'[bold white][red]Não foi possivel[/] [green]se curar[/]! Sua vida está [yellow]100%[/][/]'
                
        if self.morto:
            return Panel(
                    f'[bold white]O {self.__class__.__name__} {self.nome} está [red]morto[/], e não se cura alguem [yellow]não vivo[/] | alvo:{self.__class__.__name__} {self.nome}[/]!',
                    title='[bold red]Cura indisponível[/]',
                    width=largura,
                    border_style='red'
                )
            
        if self.vida == self.vida_inicial:
            return Panel(mensagem_negacao, title='[bold red]Cura indisponível[/]', width=largura, border_style='bright_red')
        
        with Live(Panel('', title='[bold green]Cura[/]', width=largura, border_style='bright_green'), refresh_per_second=5) as painel:
            while self.vida < self.vida_inicial:
                vida_falta = self.vida_inicial - self.vida
                if quantidade <= 0:
                    return
                if quantidade > vida_falta:
                    self.vida += vida_falta
                    conteudo.append(f':sparkles: [bold white]{self.__class__.__name__} {self.nome} se curou! Vida atual:[/] [blue]{self.vida}[/]/[blue]{self.vida_inicial}[/]')
                else:
                    self.vida += quantidade
                    conteudo.append(f':sparkles: [bold white]{self.__class__.__name__} {self.nome} se curou! Vida atual:[/] [blue]{self.vida}[/]/[blue]{self.vida_inicial}[/]')
                    
                
                painel.update(Panel('\n'.join(conteudo), title='[bold green]Cura[/]', width=largura, border_style='bright_green'))
