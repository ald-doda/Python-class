a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))

if a > 0:
    z = b - a
elif a > -3 and a <= 0:
    z = a / 3
else:
    z = 2 * b

print(z)