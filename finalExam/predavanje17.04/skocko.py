import random
#igrice 

tref = "♣"
pik = "♠"
karo = "♦" 
skocko = "☻"
srce = "♥"

crvena = "🔴"
zuta = "🟡"
bijela = "⚪"

simboli = [tref, pik, karo, skocko, srce]

def validiraj_unos(unos):
    if len(unos)!= 4:
        return False
    if len(set(unos).difference(set(simboli))) >0:
        return False
    return True

def igra():
    tajna_kombinacija = random.choices(simboli, k=4) #4 nasumicno izabrana simbola
    print(tajna_kombinacija)
        
    broj_pokusaja=0
    while broj_pokusaja < 6:
        validan_poksaj = False
        while not validan_pokusaj:
            pokusaj = input("Unesite kombinaciju: ")
            validan_pokusaj=validiraj_unos
        
    broj_pokusaja+=1
    brojCrvenih = 0;

    for i, c in enumerate(pokusaj):
         if c == tajna_kombinacija[i]:
            brojCrvenih+=1
        
    brojZutih = 0
    brojPogodjenih=0
    tajna_kombinacija_copy = tajna_kombinacija.copy()

    for c in pokusaj:
         if c in tajna_kombinacija_copy:
           brojPogodjenih+=1
           tajna_kombinacija_copy.remove()
        
    brojZutih = brojPogodjenih-brojCrvenih
    brojBijelih = 4 - brojCrvenih - brojZutih
    
    print(crvena*brojCrvenih+zuta*brojZutih+bijela*brojBijelih)
    if brojCrvenih == 4:
        print("Cestitamoe! Pogodili ste kombinaciju.")
        break
    else:
        print("Nazalost niste pogodili tajnu kombinaciju.")
        
    #treba dodati da se zavrsava ako su sve 4 na pravom mjestu

igra()

            
