a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if ((min(a,b)) /((min(pow(a,2),pow(b,2))+ 6))) == 0:
    print("Nije moguce dijeliti sa nulom.")
else:
    izraz = min(a,b) / (min(pow(a,2),pow(b,2))+ 6)
    print(izraz)