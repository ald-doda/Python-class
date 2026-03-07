a = float(input("Unijeti broj a: "))
b = float(input("Unijeti  broj b: "))

donji_dio = (2 + max(pow(a,2), pow(b,2)))

if donji_dio == 0:
    print("Nije moguce dijeliti sa nulom.")
else:
    izraz = (0.5 - min(a,b)) / donji_dio
    print(izraz)