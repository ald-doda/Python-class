a = int(input("Unesite vrijednost a: "))
b = int(input("Unesite vrijednost b: "))

if a > 1:
    z = b / a
elif a > -6 and a <= 1:
    z = a + 3
else:
    z = a + b

print(z)