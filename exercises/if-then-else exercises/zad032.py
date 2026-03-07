from math import sqrt

x = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))
z = int(input("Unesite vrijednost z: "))

if (sqrt(x - y + pow(z, 2))):
    izraz = sqrt(x - y + pow(z, 2))
    print("Rjesenje izraza je: ", izraz,".")
else:
    print("Nedefinisano rjesenje. (imaginaran broj)")