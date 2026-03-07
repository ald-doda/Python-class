from math import sqrt
x = int(input("Unesite vrijednost broja x: "))

if sqrt(x) >= 0:
    izraz = sqrt(x)
    print("Rjesenje izraza je: ", izraz,".")
else:
    print("Nedefinisan.")