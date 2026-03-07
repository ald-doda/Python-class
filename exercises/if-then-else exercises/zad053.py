a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if b >= 0:
    print(2 * min(a,b))
else:
    print(min(pow(a,2),pow(b,2)))