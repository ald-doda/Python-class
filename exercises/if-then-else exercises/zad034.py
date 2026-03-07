from math import sqrt

x = int(input("Unesite vrijednost x: "))
b = int(input("Unesite vrijednost b: "))
c = int(input("Unesite vrijednost c: "))

if (2 * pow(x, 2) - 3 * b * c * x) >= 0:
    izraz = sqrt(2 * pow(x, 2) - 3 * b * c * x)
    print("Rjesenje izraza je: ", izraz,".")
else:
    print("Nedefinisano rjesenje (imaginaran broj).")