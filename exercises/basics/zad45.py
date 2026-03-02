from math import sqrt

a = int(input("Unesite vrijednosti a: "))
b = int(input("Unesite vrijednosti b: "))
c = int(input("Unesite vrijednosti c: "))

obim = a + b + c
s = obim / 2
p = sqrt(s*(s-a)*(s-b)*(s-c))

print("Obim trougla je ", obim,",","a povrsina je ", p,".")