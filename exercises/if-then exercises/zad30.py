a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

sum = a + b

if sum < 10 and sum > -10:
    print("Suma brojeva je jednocifrena.")
else:
    print("Suma dva ucitana broja je visecifrena.")