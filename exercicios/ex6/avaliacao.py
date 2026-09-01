class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
    
    # Metodo acessores
    def get_nota(self): # -> Metodo Getter
        return self._nota
    
    def set_nota(self, valor): # -> Metodo Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Entao...A nota é invalida tem que ser de 0 a 10')