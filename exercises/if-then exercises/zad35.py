a = int(input("Unesite vrijednost broja a: "))
b = int(input("Unesite vrijednost broja b: "))

sum = a + b

if sum < 10 or sum > -10:
    print("Suma nije dvocifrena.")
else:
    print("Suma je dvocifrena.")