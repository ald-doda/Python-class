from math import sqrt
x = int(input("Unesite vrijednost x: "))
b = int(input("Unesite vrijednost b: "))
c = int(input("Unesite vrijednost c: "))

if (2 + 3* x * b * c - 4 * pow(x, 2)) >= 0:
    izraz = sqrt(2 + 3*(x * b * c) - 4 * pow(x, 2))
    print("Rjesenje je:", izraz,".")
else:
    print("Nedefinisano rjesenje (imaginaran broj).")