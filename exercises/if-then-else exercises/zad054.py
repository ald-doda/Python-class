a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a>= b:
    print(1 - min(a,b))
else:
    print(max(pow(a,2),pow(b,2)))
    