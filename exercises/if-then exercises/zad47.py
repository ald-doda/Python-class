a = int(input("Unesite vrijednost prvog broja: "))
b = int(input("Unesite vrijednost drugog broja: "))

sum = a + b

if sum % a == 0:
    print("Suma je djeljiva sa prvim brojem.")
elif sum % a != 0:
    print("Suma nije djeljiva sa prvim brojem.")
else:
    print("Greska pri unosu.")