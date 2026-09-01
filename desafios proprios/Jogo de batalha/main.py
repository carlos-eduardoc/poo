from superclasse import Personagem
from guerreiro import Guerreiro
from mago import Mago
from rich import print
from rich.panel import Panel

def main():
    p1 = Guerreiro('Ruffys', 55, 10, 45, 25)
    p2 = Mago('Zyrox', 55, 45, 15, 25)

    

    print(p1.correr())
    #print(p2.correr())

    print(p1.ativar_arma('lança'))
    print(p1.ativar_desativar_armadura()) 
    print(p1.ativar_desativar_armadura()) 
    print(p1.atacar(p2))
    print(p2.lancar_fogo(p1))
    print(p1.atacar(p2))
    
    print(p1.ativar_desativar_armadura())
    print(p2.lancar_fogo(p1))
    
    print(p2.curar(35))
    for i in range(1, 2 + 1):
        print(p1.atacar(p2))
    print(p2.curar(35))
    
    


if __name__ == "__main__":
    main()