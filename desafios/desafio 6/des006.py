#  crie uma class Gamer, que tenha nome e nick do jogador
# permitindo adicionar jogos favoritos
# e mostrar uma ficha de jogador

from rich import print
from rich.panel import Panel
from auxiliar import line

class Gamer:
    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    
    def add_favoritos(self, jogo: str):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos.sort()


    def ficha_jogador(self):
        jogos =  ''

        for jogo in self.jogos_favoritos:
            jogos += f'\n:video_game: {jogo}'

        ficha = Panel(f'[bold white]Nome real[/]: [bold black on white] {self.nome} [/] \n'
                      f'[bold white]Jogos favoritos de[/] <{self.nick}>:'
                      f'[bold dark_orange]{jogos}[/]',
                      width=45,
                      title=f'[bold white]Jogador <{self.nick}>[/]',
                      style='bold green'
                    )
        return ficha


j1 = Gamer('Joao Pedro da Silva Jefergo', '2026énosso09')
j2 = Gamer('Carlos Eduardo', 'carlosxz')

j1.add_favoritos('Fc Mobile 26')
j1.add_favoritos('God of War')
j1.add_favoritos('Brawl Stars')

j2.add_favoritos('Super Mario Bros')
j2.add_favoritos('Roblox')
j2.add_favoritos('Adverse')


print(j1.ficha_jogador())
line(50)
print(j2.ficha_jogador())