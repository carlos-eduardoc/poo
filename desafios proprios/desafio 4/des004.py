from rich import print

class Livro:
    def __init__(self, titulo:str='Sem titulo', autor:str='Sem autor'):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = True


class Biblioteca:
    def __init__(self):
        self.livros = []


    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        return f'[bold white]Você [green]cadastrou[/] o livro {livro.titulo} com sucesso![/]'


    def emprestar_livro(self, livro):
        if livro.disponibilidade:
            livro.disponibilidade = False
            return f'[bold white]Você [green]emprestou o livro {livro.titulo}, {livro.autor}[/][/]!'
        else:
            return f'[bold white]O livro {livro.titulo}, {livro.autor} [bold red]não está disponivel[/] para emprestimo[/]!'


    def devolver_livro(self, titulo):
        for l in self.livros:
            if titulo.lower() == l.titulo.lower():
                if not l.disponibilidade:
                    l.disponibilidade = True
                    return f'[bold white]O Livro {l.titulo}, {l.autor} [bold green]foi devolvido com sucesso[/][/]!'
                else:
                    return f'[bold white]O Livro {l.titulo}, {l.autor} [bold yellow]não está emprestado![/][/]'

        return f'[bold white]O livro {titulo} [bold red]não foi encontrado[/][/]!'


    def buscar_livro(self, titulo, autor):
        for l in self.livros:
            if l.titulo.lower() == titulo.lower() and l.autor.lower() == autor.lower():
                return f'[bold white]O livro {l.titulo}, {l.autor} [green]foi encontrado[/][/]!'
        return f'[bold white]O livro {titulo}, {autor} [red]não foi encontrado[/][/]!'



l1 = Livro('As cronicas de narnia', 'C.S. Lewis')
l2 = Livro('O homem mais rico da Babilonia', 'George B.C.')
biblioteca = Biblioteca()

print(biblioteca.cadastrar_livro(l1))
print(biblioteca.cadastrar_livro(l2))

print(biblioteca.emprestar_livro(l2))
print(biblioteca.buscar_livro('O homem mais rico da Babilonia', 'George B.C.'))

print(biblioteca.emprestar_livro(l2))
print(biblioteca.devolver_livro('O homem mais rico da Babilonia'))