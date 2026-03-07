x  = int(input("Unesite vrijednost x: "))
y = int(input("Unesite vrijednost y: "))

if x > y:
    x = x -2
    y = y -2
else:
    x = x + 2
    y = y + 2

print("Vrijednosti obje varijable su:", x, y,".")