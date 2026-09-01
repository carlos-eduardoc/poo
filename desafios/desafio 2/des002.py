# Crie uma class Funcionario, onde podemos cadastrar nome, setor e cargo
# criar um metodo de apresentação do funcionario.

from rich import print
from rich.panel import Panel
from rich.traceback import install
from auxiliar import line

install()
painel_1 = Panel('Funcionario'.center(40), width=45, style='bold blue')

class Funcionario:
    """
[blue]Esta classe, ela permite a nós criar um objeto que vai receber os atributos de nome, setor e cargo.
Dentro da classe tem o metodo apresentacao, ele apresenta o funcionario, informando seus dados como nome, seu setor e cargo.[/]
    """
    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def __str__(self):
        return f'[bold yellow]{self.nome} fica no setor de {self.setor}, e tem o cargo de {self.cargo}[/]'
        
    def apresentacao(self):
        print(painel_1)
        print(f'[bold red]Nome do Funcionario[/]: \t\t[bold white]{self.nome}[/] \n[bold red]Setor do Funcionario[/]: \t\t[bold white]{self.setor}[/] \n[bold red]Cargo do Funcionario[/]: \t\t[bold white]{self.cargo}[/] \n[bold red]Empresa[/]: \t\t\t[bold white]{Funcionario.empresa}[/]')


f1 = Funcionario('Carlos', 'TI', 'Especialista em Segurança Ofensiva')
f2 = Funcionario('Maria', 'TI', 'Programadora front-end')


f1.apresentacao()
line()
f2.apresentacao()
