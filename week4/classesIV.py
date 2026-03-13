#Objektno orijentisano programiranje je moguce u Pythonu:

#definisanje klasa:

class Automobil: #naziv klase 

    #definisanje konstruktora za klasu:
    def _init__(self, model, proizvodjac, godiste, snaga_motora):
        self.model = model 
        self.proizvodjac = proizvodjac
        self.godiste = godiste
        self.snaga_motora = snaga_motora

    def izracunaj_potrosnju(self, a=20, b=5):
        return self.snaga_motora*20/self.godiste*5
    
    #this se predaje kao argument svake f-je
    #u python-u se zove self i uvijek se mora sam pisati

a = Automobil("Golf 7", "VW", 2017, 130) #dodajemo novi automobil nasoj klasi
print(a.godiste) #stampa godiste
print(a.model) #stampa model
print(a.izracunaj_potrosnju(b=5.5)) #stampa formulu za potrosnju kada je b=5.5