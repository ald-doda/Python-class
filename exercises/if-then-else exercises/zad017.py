a = int(input("Unesite vrijednost a: "))

if a % 2 != 0:
    y = 1/a
else:
    y = pow((a-1), 2)

print("Vrijednost y je jednaka:", y,".")