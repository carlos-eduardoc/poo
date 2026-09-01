from rich import print

class ListadeTarefa:
    def __init__(self):
        self.tarefas = []

    
    def add_tarefas(self, titulo):
        self.tarefas.append({'titulo': titulo, 'concluida': False})
        print(f'[bold]A tarefa [bold green]{titulo}[/] foi adicionada com sucesso!')


    def concluir_tarefa(self, titulo):
        for t in self.tarefas:
            if t['titulo'] == titulo:
                t['concluida'] = True
                print(f'[bold]A tarefa [bold blue]{t['titulo']}[/] foi concluida com sucesso!')
                return    
        print(f'[bold]A tarefa [bold red]{titulo}[/] não foi encontrada!')


    

    def listar_tarefa(self):
        for t in self.tarefas:
            if t['concluida']:
                print(f":white_check_mark: [bold green]{t['titulo']}[/]")
            else:
                print(f":x: [bold red]{t['titulo']}[/]")


t1 = ListadeTarefa()
t1.add_tarefas('Estudar POO')
t1.add_tarefas('Escovar dentes')
t1.concluir_tarefa('Escovar dentes')
t1.concluir_tarefa('Estudar POO')

t1.listar_tarefa()