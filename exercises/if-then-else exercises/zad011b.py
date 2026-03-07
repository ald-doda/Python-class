a = int(input("Unesite vrijednosti pocetne tacke: "))
b = int(input("Unesite vrijednosti krajnje tacke: "))

distanca = b - a

if distanca >= 0:
    print("Distanca je jednaka:", distanca,".")
else:
    dis = -distanca
    print("Distanca je jednaka:", dis,".")