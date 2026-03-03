import random

n = random.randint(-9, 9)

print("Nasumican broj je: ", n,".")

if n % 7 != 0:
    print("Broj nije djeljiv sa 7.")
else:
    print("Broj je djeljiv sa 7.")