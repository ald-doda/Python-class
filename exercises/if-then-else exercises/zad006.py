from math import sqrt
a = int(input("Unesite vrijednost a: "))

if a > 0:
    z = sqrt(a)
else:
    z = pow(a, 2)

print("Vrijednost z je jednaka: ", z,".")