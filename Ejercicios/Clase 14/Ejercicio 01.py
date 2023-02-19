class Cetaceo:
    def __init__(self, notas, viveEn, peso):
        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso
        
    def nacer(self):
        pass
    
    def nadar(self):
        pass
    
class Mamifero(Cetaceo):
    def __init__(self, notas, viveEn, peso, cantMamas, esperanzaDeVida):
        super().__init__(notas, viveEn, peso)
        self.cantMamas = cantMamas
        self.esperanzaDeVida = esperanzaDeVida
        
    def mamar(self):
        pass
    
    def nacer(self):
        pass
    
f = Mamifero(2, 32, 432, 23, 4)

f.nacer()