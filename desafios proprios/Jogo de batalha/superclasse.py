""" 
Crie uma classe base Personagem com nome, vida, ataque e defesa. Crie
subclasses como Guerreiro e Mago, cada uma com uma habilidade própria.

Implemente um combate entre dois personagens em turnos. O dano deve ser
de pelo menos 1 e o programa deve informar o vencedor. Use __repr__ para
uma representação útil dos personagens durante os testes.


"""
import time
from rich import print
from rich.panel import Panel
from rich.live import Live
from time import sleep as sl

LARGURA_PAINEL = 90


class Personagem:
    def __init__(self, nome='Personagem desconhecido', vida=55, ataque=15, defesa=35, energia=100):
        self.nome:str = nome
        self.vida:int = vida
        self.ataque:int = ataque
        self.defesa:int = defesa
        self.energia:int = energia
        self.distancia:float = 0
        self.morto:bool = False
        
    
    def __repr__(self):
        return f'Classe: {self.__class__.__name__} \nNome: {self.nome} \nVida: {self.vida} \nAtaque: {self.ataque} \nDefesa: {self.defesa} \nEnergia: {self.energia} \nTa morto? {self.morto}'
    
    def __rich__(self):
        caracteristicas = (
            f'[bold cyan]Classe:[/] {self.__class__.__name__}\n'
            f'[bold cyan]Personagem:[/] {self.nome}\n\n'
            f'[bold red]Vida atual:[/] {self.vida} — indica quanto dano o personagem ainda suporta.\n'
            f'[bold yellow]Defesa atual:[/] {self.defesa} — absorve o dano antes de atingir a vida.\n'
            f'[bold orange1]Ataque:[/] {self.ataque} — define o dano causado ao alvo.\n'
            f'[bold blue]Energia:[/] {self.energia} — é usada para correr.\n'
            f'[bold magenta]Distância:[/] {self.distancia} km — determina se o alvo está ao alcance.'
        )
        return Panel(
            caracteristicas,
            title=f'Características de {self.nome}',
            width=LARGURA_PAINEL,
            border_style='bright_blue'
        )



    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida > 0:
            return False
        else:
            self.morto = True
            return True

    def recarregar_energia(self):
        self.energia = 100
        return self.energia
    

    def executar_ataque(self, alvo, dano, alcance):
        if self.morto:
            return

        if alvo.morto:
            return Panel(
                        f'[bold white]O alvo está [red]morto[/], e não se ataca alguem [yellow]não vivo[/] | alvo:{alvo.__class__.__name__} {alvo.nome}[/]!',
                        title='[bold red]Ataque bloqueado[/]',
                        width=LARGURA_PAINEL,
                        border_style='red'
                    )
                    
        diferenca = abs(alvo.distancia - self.distancia)
        if diferenca <= alcance:
            mensagem_ataque = f'[bold white]{self.__class__.__name__} {self.nome} atacou {alvo.__class__.__name__} {alvo.nome}![/]\n'
            alvo.defesa -= dano
            if alvo.defesa <= 0 and alvo.defesa + dano > 0:
                morreu = alvo.receber_dano(dano)
                if morreu:
                    return Panel(f'{mensagem_ataque}[bold white]O alvo {alvo.nome} [red]morreu[/] pelo [yellow]{self.nome}[/][/]!',
                                    title='[bold red]Alvo derrotado[/]',
                                    width=LARGURA_PAINEL,
                                    border_style='red'
                                )
                else:
                    return Panel(f'{mensagem_ataque}[bold white]O {self.__class__.__name__} {self.nome} tirou toda a defesa de {alvo.__class__.__name__} {alvo.nome}[/]!',
                                    width=LARGURA_PAINEL,
                                    border_style='bright_yellow',
                                    title=f'{self.__class__.__name__} {self.nome}'
                                )
            elif alvo.defesa > 0:
                    return Panel(f'{mensagem_ataque}[bold red]-{dano}[/] [bold white]:shield: Defesa atual do alvo é de[/] [blue]{alvo.defesa}[/]',
                        title=f'{self.__class__.__name__} {self.nome}',
                        width=LARGURA_PAINEL,
                        border_style='cyan'
                    )
        
            morreu = alvo.receber_dano(dano)
            if morreu:
                return Panel(
                    f'{mensagem_ataque}[bold white]O alvo {alvo.nome} [red]morreu[/] pelo [yellow]{self.nome}[/][/]!',
                    title='[bold red]Alvo derrotado[/]',
                    width=LARGURA_PAINEL,
                    border_style='red'
                    )
            else:
                return Panel(
                    f'{mensagem_ataque}[bold red]-{dano}[/] :heart: [bold white]Vida atual do alvo é de[/] [blue]{alvo.vida}[/]',
                    title=f'{self.__class__.__name__} {self.nome}',
                    width=LARGURA_PAINEL,
                    border_style='magenta'
                    )
                
        else:
            return Panel(
                f'[bold white]Você está a mais de [red]{diferenca}km[/] de distancia do alvo, sendo impossivel de acertar o alvo {self.__class__.__name__} {self.nome}[/]!',
                title='[bold orange1]Fora de alcance[/]',
                width=LARGURA_PAINEL,
                border_style='orange1'
                )

    def correr(self):
        conteudo = []
        mensagem_negacao = f'[bold white]Não foi possivel [blue]correr[/], o [orange1]{self.__class__.__name__} {self.nome}[/] está com [blue on blue] {self.energia} [/] de energia![/]'
        with Live(Panel('', title='[bold blue]Corrida[/]', width=LARGURA_PAINEL, border_style='bright_blue'), refresh_per_second=5) as painel:
            for c in range(1, self.energia):
                if self.energia >= 15:
                    self.distancia += 1
                    self.energia -= 2
                    mensagem_negacao = f'[bold white]Não foi possivel [blue]correr[/], o [orange1]{self.__class__.__name__} {self.nome}[/] está com [blue on blue] {self.energia} [/] de energia![/]'

                    conteudo.append(
                        f'[bold white]{self.__class__.__name__} {self.nome} esta [blue]correndo[/],  está com [blue on blue] {self.energia} [/] de energia!, e está a [red]{self.distancia}km[/] de distancia de seus inimigos[/]'
                        )
                    
                    painel.update(Panel('\n'.join(conteudo), title='[bold blue]Corrida[/]', width=LARGURA_PAINEL, border_style='bright_blue'))
                    sl(1)

            if self.energia < 15:
                return Panel(mensagem_negacao, title='[bold yellow]Corrida encerrada[/]', width=LARGURA_PAINEL, border_style='yellow')


    def atacar(self, alvo):
        return self.executar_ataque(alvo, self.ataque, 5)

        
