a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a >= 0:
    print(max(a,b))
else:
    print(max(pow(a,2),pow(b,2)))