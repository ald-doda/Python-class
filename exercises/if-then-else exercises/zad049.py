a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a >= 0:
    print(min(a,b))
else:
    print(2 * min(a,b))