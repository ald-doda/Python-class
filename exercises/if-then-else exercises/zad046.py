a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a > b:
    a = a * 2
    b = b / 3
else:
    b = b * 2
    a = a / 3

print(a, b)