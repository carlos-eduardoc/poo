from rich import print
from rich.panel import Panel

class Personagem:
    def __init__(self, nome, vida, ataque, defesa, distancia=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.distancia = distancia
        self.morto = False


    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida > 0:
            return False
        else:
            self.morto = True
            return True

    
    def atacar(self, alvo):
        if self.morto:
            return
        else:
            if not alvo.morto:
                diferenca = abs(alvo.distancia - self.distancia)
                if diferenca < 5:
                    alvo.defesa -= self.ataque
                    if alvo.defesa <= 0 and alvo.defesa + self.ataque > 0:
                        morreu = alvo.receber_dano(self.ataque)
                        if morreu:
                            return Panel(f'[bold white]O alvo {alvo.nome} [red]morreu[/] pelo [yellow]{self.nome}[/][/]!')
                        else:
                            return Panel(f'[bold white]O {self.__class__.__name__} {self.nome} tirou toda a defesa de {alvo.__class__.__name__} {alvo.nome}[/]!')
                    elif alvo.defesa > 0:
                        return Panel(f'[bold red]-{self.ataque}[/] [bold white]:shield: Defesa atual do alvo é de[/] [blue]{alvo.defesa}[/]')

                    morreu = self.receber_dano(self.ataque)
                    if morreu:
                        return Panel(f'[bold white]O alvo {alvo.nome} [red]morreu[/] pelo [yellow]{self.nome}[/][/]!')
                    else:
                        return Panel(f'[bold red]-{self.ataque}[/] :heart: [bold white]Vida atual do alvo é de[/] [blue]{alvo.vida}[/]')
                else:
                    return Panel(f'[bold white]Você está a mais de [red]{diferenca}km[/] de distancia do alvo, sendo impossivel de acertar o alvo {self.__class__.__name__} {self.nome}[/]!')
            else:
                return Panel(f'[bold white]O alvo está [red]morto[/], e não se ataca alguem [yellow]não vivo[/] | alvo:{alvo.__class__.__name__} {alvo.nome}[/]!')
                

# ============================================
# TESTE: reproduzindo o cenário do bug
# ============================================
print("=== Cenário: defesa baixa E vida baixa ao mesmo tempo ===\n")

heroi = Personagem(nome="Heroi", vida=100, ataque=5, defesa=10, distancia=0)
inimigo = Personagem(nome="Inimigo", vida=4, ataque=3, defesa=3, distancia=0)

print(f"ANTES do ataque -> vida={inimigo.vida}, defesa={inimigo.defesa}, morto={inimigo.morto}")

resultado = heroi.atacar(inimigo)
print(f"Mensagem retornada: {resultado}")

print(f"DEPOIS do ataque -> vida={inimigo.vida}, defesa={inimigo.defesa}, morto={inimigo.morto}")

print()
if inimigo.vida <= 0 and not inimigo.morto:
    print("BUG CONFIRMADO: vida <= 0 mas 'morto' continua False!")
else:
    print("Não houve inconsistência neste teste.")