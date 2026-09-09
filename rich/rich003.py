#  Table tabelas, chamando o objeto da class Table ele, cria uma tabela.
# Para add novas colunas na tabela usamos obj.add_column
# Para add linha a coluna, usamos add_row
# add_section ele cria uma linha divisoria
# justify ele permite colocar o titulo das colunas, center, right, left

# # Para nomear, dentro da intanciação colocamos title='titulo' 


from rich import print
from rich.table import Table
from rich.panel import Panel

painel = Panel('[green]Tabela d[/][yellow]e Preços[/]'.center(55), style='blue', width=40)
tabela = Table(style='blue', width=45)


# Colunas
tabela.add_column('[yellow]Nome[/]', justify='center')
tabela.add_column('[yellow]Preço[/]', justify='center')

# Linhas 
tabela.add_row('[green]Leite[/]', '[red]R$12,50[/]')
tabela.add_section()
tabela.add_row('[green]Ovo[/]', '[red]R$10,00[/]')


print(painel)
print(tabela)