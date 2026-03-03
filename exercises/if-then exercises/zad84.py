import random

n  = random.randint(-9, 9)

print("Nasumicno generisani broj je: ", n,".")

if n % 7 == 0:
    print("Broj je djeljiv sa 7.")
else:
    print("Broj nije djeljiv sa 7.")