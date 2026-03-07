from math import sqrt
a = int(input("Unesite vrijednost a: "))

if a % 2 != 0:
    y = 1/a
else:
    y = sqrt(a + 1)
print("Vrijednost y je jednaka:", y,".")