# rich - painel, ele cria um painel bem util e ajuda na visibilidade nas caixas de texto.

from rich import print
from rich.panel import Panel

caixa = Panel(f'[green]{"Ola, Mundo! :earth_americas:".center(50)}[/][blue]\nHoje temos que falar de Neymar Junior. \nNeymar se despediu da Seleção Brasileira, encerrando uma era que marcou o futebol nacional.\nFicam as memórias, os momentos inesquecíveis e seu legado na história da amarelinha.[/]',
                title='[white]Recado para Neymar![/]',
                style='yellow', 
                width=45
            )

print(caixa)