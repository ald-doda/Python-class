prosjek = float(input("Unesite prosjek: "))

if prosjek >= 4.5:
    print("Odlican")
elif prosjek < 4.5 and prosjek >= 3.5:
    print("Vrlodobar")
elif prosjek < 3.5 and prosjek >= 2.5:
    print("Dobar")
elif prosjek < 2.5 and prosjek >= 1.5:
    print("Dovoljan")
elif prosjek < 1.5:
    print("Nedovoljan")
else:
    print("Greska pri unosu:")