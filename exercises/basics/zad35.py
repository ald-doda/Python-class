from math import sqrt

a = int(input("Unesite vrijednost stranice a: "))
p = int(input("Unesite vrijednost povrsine p: "))

b = float((p - 2 * a)/2)
d = sqrt(pow(a,2) + pow(b, 2))

print("Stranica b iznosi", b,"dijagonala d iznosi", d,".")

