import random
def validiraj_izraz(izraz, cifre, srednjiBroj, velikiBroj):
    for c in izraz:
        if not c.isdigit() and c not in ["(", ")", "+", "*", "*", "/"]:
            return False
    
    trenutniBroj=""
    for c in izraz:
        if c.isdigit():
            trenutniBroj+=c
        elif trenutniBroj != "":
            trenutniBroj=int(trenutniBroj)
            if trenutniBroj in cifre:
                cifre.remove(trenutniBroj)
            elif trenutniBroj == srednjiBroj:
                srednjiBroj= float("-inf")
            elif trenutniBroj == velikiBroj:
                velikiBroj = float("-inf")
            else:
                return False
    
    trenutniBroj=""
    
    if trenutniBroj!="":
        komentar="ponovi ono gore??"
        
    return True

def igra():
    
    trazeniBroj = random.randint()
    cifre = [random.randint(1, 9) for _ in range(4)] #list comprehensive? generise listu bez elem.append()
    srednjiBroj = random.choice([10, 15, 20])
    velikiBroj = random.choice([25, 50, 75, 100])
    
    print(""*15+"_______")
    print("| " + "%03d" % trazeniBroj + " |")
    print(""*15+"_______")
    
    print("| "+ "  |".join([str(c) for c in cifre]) + " |", end= "      ")
    print("| "+str(srednjiBroj)+" |", end="   ")
    print("| "+str(velikiBroj)+"  |")
    
    izraz = input("Unesite aritmeticki izraz")
    if not validiraj_izraz(izraz, cifre, srednjiBroj, velikiBroj):
        print("Vas izraz nije validan.Dobili ste 0 poena")
        return
    vrijednost = eval(izraz)
    if vrijednost == trazeniBroj:
        print("Svaka cast! Pogodili ste trazeni broj")
    else:
        print("Niste pogodili broj, udaljeni ste za:", + abs(vrijednost-trazeniBroj))
    
#vjesala
    
    
    
    
if __name__ == "__main__":
    igra()
