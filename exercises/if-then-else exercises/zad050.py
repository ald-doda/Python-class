a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a >= 0:
    print(min(a,b))
else:
    print(min(pow(a,2),pow(b,2)))