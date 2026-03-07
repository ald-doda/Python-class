x = int(input("Unesite vrijednost x:"))

if x <= -2:
    y = x + 2
elif x > -2 and x < 2:
    y = 2
else:
    y = x - 2

print(y)