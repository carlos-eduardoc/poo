# criando a classe Caneta com atributos como cor e estado (tampada ou destampada). 
# Você aprenderá a implementar métodos como escrever, tampar, destampar e quebrar linha, 
# além de utilizar a biblioteca Rich para imprimir textos coloridos no terminal.
# Um exercício prático que reforça os conceitos de classes, atributos, métodos e instâncias em Python.
 # acima estaa a descrição do exercicio porem esta pronta do guanabara

from rich import print
from auxiliar import line
from deep_translator import GoogleTranslator

class Caneta:
    def __init__(self, cor: str):
        self.cor = cor
        self.destampada = False

    
    def destampar(self):
        self.destampada = not self.destampada


    def escrever(self, msg):
        if self.destampada == False:
            print(':stop_sign: [bold red]Para escrever é preciso destampar a caneta![/] :stop_sign:')
        else:
            print(f'[{self.traduzir()}] {msg}[/]', end='')
    

    def traduzir(self):
        tradutor = GoogleTranslator(source='pt', target='en')
        traducao = tradutor.translate(self.cor)
        return traducao

    def quebra_linha(self, linhas=1):
        print(f'{"\n" * linhas }') 



c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')
c4 = Caneta('laranja1')
c5 = Caneta('negrito roxo3')

c1.destampar()
c2.destampar()
c3.destampar()
c4.destampar()
c5.destampar()

c1.escrever('O ceu é azul')
c1.quebra_linha(1)
c2.escrever('O sangue é vermelho')
c2.quebra_linha()
c3.escrever('A grama é verde')
c3.quebra_linha()
c4.escrever('O sol tem tom visivel de laranja')
c4.quebra_linha()
c5.escrever('O Espaço é roxo')