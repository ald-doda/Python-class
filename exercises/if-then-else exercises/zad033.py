from math import sqrt

x = int(input("Unesite vrijednost x: "))

if (2 * x + sqrt(pow(x, 2) + 3 * x - 10)) > 10:
    izraz = 2 * x + sqrt(pow(x,2) + 3 * x - 10)
    print("Rjesenje izraza je: ", izraz,".")
else:
    print("Nedefinisano rjesenje (imaginaran broj).")