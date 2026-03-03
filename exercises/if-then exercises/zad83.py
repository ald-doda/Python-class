import random

n = random.randint(-9, 9)

print("Nasumicno generisani broj je: ", n,".")

if n % 3 != 0:
    print("Broj nije djeljiv sa tri.")
else:
    print("Broj je djeljiv sa tri.")