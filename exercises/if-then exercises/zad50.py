a = float(input("Unesite broj a: "))

cA = int(a)

if a != cA:
    if cA % 2 == 0:
        print("Broj a je paran", cA,".")
        tS = pow(cA,3)
        print("Treci stepen broja a je ", tS,".")
    elif cA % 2 != 0:
        print("Broj a nije paran.")
else:
    print("Broj a je cio broj.")