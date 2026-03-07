a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if ((2 * max(a,b))  / (1 + (max(pow(a,2),pow(b,2))))) == 0:
    print("Nije moguce dijeliti sa nulom.")
else:
    izraz = (2 * max(a,b)) / (1 + (max(pow(a,2),pow(b,2))))
    print(izraz)