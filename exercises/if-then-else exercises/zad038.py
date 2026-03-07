x  = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))

if y > x:
    x = x - 1
    y = x + 2
else:
    x = x + 1
    y = x - 2

print("Vrijednosti obje varijable su:", x, y,".")