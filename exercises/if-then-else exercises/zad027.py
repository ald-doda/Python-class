x = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))
z = int(input("Unesite vrijednost z: "))

if ((x - y) / (2*x - y * z)) == 0:
    print("Djeljenje sa nulom nije moguce.")
else:
    izraz = (x - y) / (2*x - y * z)
    print("Rjesenje izraza je", izraz,".")