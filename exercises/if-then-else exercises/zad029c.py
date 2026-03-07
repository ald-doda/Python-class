x = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))
z = int(input("Unesite vrijednost z: "))

if ((x-y+pow(z,2)) / (x* y + 2 * y * z)) == 0:
    print("Djeljenjeje sa nulom nije moguce.")
else: 
    izr = (x-y+pow(z,2)) / (x* y + 2 * y * z)
    print("Rjesenje izraza je: ", izr,".")