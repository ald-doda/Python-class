a = int(input("Unijeti broj a: "))
b = int(input("Unijeti  broj b: "))

if a > b:
    if a % 2 != 0:
        print('Neparan je veci broj.')
    else:
        print('Paran je veci broj')
else:
    if b % 2 != 0:
        print('Neparan je veci broj.')
    else:
        print('Paran je veci broj')