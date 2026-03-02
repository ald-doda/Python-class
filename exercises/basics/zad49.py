from math import sqrt
a = int(input("Unesite vrijednost stranice a: "))
b = int(input("Unesite vrijednost stranice b: "))

c = sqrt(pow(a, 2) + pow(b, 2))
p = a * b / 2

print("Hipotenuza je jednaka ", c,", a povrsina ", p,".")