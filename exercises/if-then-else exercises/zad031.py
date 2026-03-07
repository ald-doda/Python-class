from math import sqrt
x = int(input('Unesite vrijednost x: '))

if x >= 0:
    izraz = 2/3 * sqrt(x)
    print("Rjesenje izraza je: ", izraz,".")
else:
    print("Nedefinisan.")