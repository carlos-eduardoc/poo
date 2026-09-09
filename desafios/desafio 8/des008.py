# crie um controle remoto, onde simularemos o funcionamento de um controle simples
# canal, volume, ligar e desligar

 # < CH1 >  - VOL1 +

# entao vamos fazer um 'diagrama'
# class remoto:


from rich import print
from rich.panel import Panel
from time import sleep as sl
import os

class Controle:
    canal_min = 1
    canal_max = 5
    vol_min = 0
    vol_max = 5

    def __init__(self, canal, volume, nome):
        self.canal = canal
        self.volume = volume
        self.nome = nome
        self.ligada = False


    def ligar_desligar(self):
        self.ligada = not self.ligada


    def display(self):
        conteudo = ''
        if not self.ligada:
            conteudo = f':prohibited: [bold red]A TV está desligada[/] :prohibited:'.center(75)
        else:
            conteudo = f'CANAL = '

            if self.canal > Controle.canal_max:
                self.canal = Controle.canal_min
            if self.canal < Controle.canal_min:
                self.canal = Controle.canal_max

            for canal in range(Controle.canal_min, Controle.canal_max + 1):
                if canal == self.canal:
                    conteudo += f'[yellow on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            
            conteudo += f'\nVOLUME = '
            if self.volume < Controle.canal_min:
                self.volume = Controle.canal_min
            if self.volume > Controle.canal_max:
                self.volume = Controle.canal_max

            for vol in range(Controle.vol_min, Controle.vol_max + 1):
                if vol <= self.volume:
                    conteudo += f'[cyan on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'

        painel_tv = Panel(conteudo, width=50, title=f'[ TV {self.nome}]', style='bold white')
        print(painel_tv)

    def controle(self):
        if not self.ligada:
            self.display()
        else:  
            while True:
                self.display()
                escolha = input(str(f'< CH{self.canal} >  - VOL{self.volume} + '))
                if escolha == '>':
                    self.canal += 1
                elif escolha == '<':
                    self.canal -= 1
                elif escolha == '+':
                    self.volume += 1
                elif escolha == '-':
                    self.volume -= 1
                elif escolha == '@':
                    self.ligada = not self.ligada
                elif escolha == '0':
                    break
                else:
                    print(':prohibited: [bold red]Você digitou uma opção invalida! digite <, >, +, -, @ ou 0')
                    sl(0.55)
                sl(0.45)
                os.system("cls" if os.name == "nt" else "clear")


co1 = Controle(1, 1, 'Quarto')
co1.ligar_desligar()
co1.controle()

co2 = Controle(2, 3, 'Sala')
co2.ligar_desligar()
co2.controle()