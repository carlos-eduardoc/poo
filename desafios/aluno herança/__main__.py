from pessoa import Pessoa
from aluno import Aluno
from rich import inspect


def main():
    aluno = Aluno('Carlos', 1995)
    try:
        aluno.curso = 'ENG'
    except Exception as ex:
        print(ex)
    
    try:
        aluno.add_curso('MODAU')
    except Exception as ex:
        print(ex)
    
    try:    
        aluno.curso = 'MODAU'
    except Exception as ex:
        print(ex)
        
    try:
        aluno.add_curso('ADS')
    except Exception as ex:
        print(ex)
        
    inspect(aluno, private=True, methods=True)


if __name__ == '__main__':
    main()