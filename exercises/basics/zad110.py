n = int(input("Unesite vrijednost dvocifrenog broja n: "))

d = n//10
j = n%10

pro = d * j
kol = j / d

print("Proizvod cifara je: ", pro,", a kolicnik", kol,".")