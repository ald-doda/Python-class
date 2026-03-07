a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

donji_dio = max(pow(a,2), pow(b,2))
if donji_dio == 0:
    print("Nije moguce dijeliti sa nulom.")
else:
    izraz = (min(a,b) / (max(pow(a,2),pow(b,2))))
    print(izraz)