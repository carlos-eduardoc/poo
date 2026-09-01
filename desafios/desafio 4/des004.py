# Crie uma class Churrasco, onde é possivel informar quantas pessoas vao ir, quanto de carne deve ser comprado
# o custo total do churras e preço por pessoa

# informações necessarias: consumo de 400 g por pessoa, R$82,50/kg 

from rich import print
from rich.panel import Panel
from auxiliar import line

class Churrasco:
    kg_pe:float = 0.400 # g consumido por pessoa
    kg_pr:float = 82.40 # Preço do kg

    
    def __init__(self, titulo, qntd_pessoas):
        self.quantidade_pessoas = qntd_pessoas
        self.titulo = titulo
        Churrasco.kg_pe
        Churrasco.kg_pr
    

    def __str__(self):
        return f'Esse é o {self.titulo}, com {self.quantidade_pessoas} convidados!'


    def analisar(self):
        recomendacao = self.quantidade_pessoas * Churrasco.kg_pe
        total = recomendacao * Churrasco.kg_pr
        valor_pessoa = total / self.quantidade_pessoas
        conteudo = f'[white]Analisando o Churras da vez com [bold blue]{self.quantidade_pessoas}[/] convidados \nCada participante deve comer [bold orange3]400 gramas[/], e cada [bold orange3]Kg custa R$82,40[/] \n[bold yellow]Recomendado[/]: [bold]comprar {recomendacao:.3f} gramas de carne[/] \nO [bold blue]custo total[/] deste churrasco seria [bold red]R${total:,.2f}[/] \nCada pessoa iria ter que pagar [bold green]R${valor_pessoa:,.2f}[/]'
        
        analise = Panel(conteudo,
                        title=f'[bold white]{self.titulo}[/]',
                        width=60,
                        style='bold orange1'
                        )
        return analise



c1 = Churrasco('Chuuras do bao', 147)
c2 = Churrasco('Opa', 5)

line(70)
print(c1.analisar())
line(70)
print(c2.analisar())
line(70)
#print(c1)