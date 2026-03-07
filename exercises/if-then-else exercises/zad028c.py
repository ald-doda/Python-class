a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))
c= int(input("Unesite vrijednost c: "))

if ((a + 2 * b + c) / (b + a + 3* c)) == 0:
    print("Djeljenje sa nulom nije moguce.")
else:
    izr = (a + 2 * b + c) / ( b + a + 3 * c)
    print("Rjesenje izraza je: ", izr,".")
