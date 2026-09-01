from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome, salario_bru=0):
        self.nome = nome
        self.bruto_sal = salario_bru
        self.salario_min = 1612
        self.inss = (7.5 * self.bruto_sal) / 100
        self.salario = None
    
    
    @abstractmethod
    def calc_sal(self):
        pass
    
    
    def analisar_sal(self):
        qntd_min = self.salario / self.salario_min
        conteudo = f'[bold white]O salario de [bold blue]{self.nome}[/] ([bold red]{self.__class__.__name__}[/]) é de [bright_green]R${self.salario:.2f}[/] e corresponde a [yellow]{qntd_min:.1f} salario minimos[/][/]'
        print(Panel(conteudo, title='[bold white]Analise de salario[/]', width=55))



class FuncHorista(Funcionario):
    def __init__(self, nome, valor_h, qntd_h):
        super().__init__(nome)
        self.valor_h = valor_h
        self.qntd_h = qntd_h
        self.salario_bruto = valor_h * qntd_h
        
    
    def calc_sal(self):
        drs = self.salario_bruto / 6 # = 1/6 de descanso é 600
        self.salario = (self.salario_bruto + drs) - self.inss
        return self.salario


class FuncMensalista(Funcionario):
    def __init__(self, nome, salario_bru):
        super().__init__(nome, salario_bru)
    
    
    def calc_sal(self):
        self.salario = self.bruto_sal - self.inss
        return self.salario