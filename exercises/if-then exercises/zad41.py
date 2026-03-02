a = int(input("Unesite vrijednosti broja a: "))

if a < 100 and a > 9:
    print("Broj je dvocifren.")
elif a < 1000 and a > 99:
    print("Broj je trocifren.")
else:
    print("Broj nije ni dvocifren, ni trocifren.")