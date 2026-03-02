a = int(input("Unesite vrijednost broja a: "))
b = int(input("Unesite vrijednost broja b: "))

sum = a + b

if sum < 100 and sum > 9:
    print("Suma je dvocifrena.")
elif sum < 1000 and sum > 99:
    print("Suma je trocifrena.")
else:
    print("Suma nije ni dvocifrena, ni trocifrena.")