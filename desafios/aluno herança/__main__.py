from pessoa import Pessoa
from aluno import Aluno
from rich import inspect


def main():
    aluno = Aluno('Carlos', 1995)
    aluno.curso = 'ENG'
    aluno.add_curso('MODAU')
    inspect(aluno, private=True, methods=True)
    
    aluno.curso = 'MODAU'
    
    inspect(aluno, private=True, methods=True)

    
    
    
    
        
if __name__ == '__main__':
    main()