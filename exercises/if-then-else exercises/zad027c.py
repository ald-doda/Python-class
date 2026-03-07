a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))
c = int(input("Unesite vrijednost c: "))

if ((a + b + c) / (2*b + a + c)) == 0:
    print("Djeljenje sa nulom nije moguce.")
else:
    izraz = (a + b + c) / (2 * b + a + c)
    print("Rjesenje izraza je", izraz,".")