a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if ((1 - min(a,b)) / (1 + max(pow(a,2),pow(b,2)))) == 0:
    print("Nije moguce obaviti djeljenje sa nulom.")
else:
    izraz = (1 - min(a,b)) / (1 + max(pow(a,2), pow(b,2)))
    print(izraz)