a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))
d = int(input("Unesite vrijednost d: "))

if ((a+d) / (2*b - d - a)) == 0:
    print("Djeljenje sa nulom nije moguce.")
else:
    v1 = (a+d)/(2*b - d - a)
    print("Rjesenje izraza je: ", v1,".")