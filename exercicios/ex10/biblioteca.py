class Biblioteca:
    def __init__(self):
        self.biblioteca = []
    
    def __add__(self, livro):
        self.biblioteca.append(livro)
        return self
    
    def __len__(self):
        return len(self.biblioteca)
    
    