a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))

if ((2 * a + b) / (2*b - 3 * a)) == 0:
    print("Djeljenje sa nulom nije moguce.")
else:
    izraz = (2 * a + b) / (2 * b - 3 * a)
    print("Rjesenje izraza je", izraz,".")