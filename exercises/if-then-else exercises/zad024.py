s = int(input("Unesite koliko  je sati:"))

if s >= 0 and s <= 8:
    print("Dobro jutro.")
elif s>= 9 and s <= 18:
    print("Dobar dan.")
else:
    print("Dobro vece.")