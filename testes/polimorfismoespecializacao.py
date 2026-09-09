class MaeJaciara:
    def fazer_pudim(self):
        print("Pudim clássico com leite condensado e calda.")
    def fritar_coxinha(self):
        print("Coxinha fritada no óleo de soja.")
        
class FilhoMateus(MaeJaciara):         
    # Mateus herda o pudim da mãe, mas especializa a coxinha
    def fritar_coxinha(self):
        print("Coxinha feita na Air Fryer (mais saudável).")
        
class FilhaMonica(MaeJaciara):
    # Mônica herda a coxinha, mas especializa o pudim
    def fazer_pudim(self):
        print("Pudim gourmet com Leite Ninho e Nutella.")
        
# isto é override porem de refinamento
# Demonstração
mateus = FilhoMateus()
monica = FilhaMonica()
mateus.fazer_pudim()
mateus.fritar_coxinha()
monica.fazer_pudim()
monica.fritar_coxinha()
# Herdado da mãe
# Sobrescrito (Override)
# Sobrescrito (Override)
# Herdado da mãe