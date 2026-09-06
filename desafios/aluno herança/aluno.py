from pessoa import Pessoa
NENHUM = None


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso=NENHUM):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
        self._curso = curso
        
        esta_na_lista = False
        for cs in self.cursos_oficiais:
            if curso == cs:
                esta_na_lista = True
                return   
        if esta_na_lista == False:
            self._curso = NENHUM
            
    
    @property
    def curso(self):
        return f'{self._nome} faz o curso {self._curso}'
    
    @curso.setter
    def curso(self, valor:str):
        for cs in self.cursos_oficiais:
            if valor == cs:
                self._curso = valor
                return
        else:
            raise ValueError('Curso invalido! Não está na lista')

    
    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        
        if curso in self.cursos_oficiais:
            raise ValueError('O curso já está na lista oficial!')
        if len(curso) <= 5 and len(curso) > 1:
            self.cursos_oficiais.append(curso.upper())
        else:
            raise ValueError('O curso digitado tem mais de 5 SIGLAS!')
