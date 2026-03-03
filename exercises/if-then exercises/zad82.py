import random

n = random.randint(-9, 9)

print("Nasumican broj je: ", n,".")

if n % 3 == 0:
    print("Broj je djeljiv sa tri.")
else:
    print("Broj nije djeljiv sa tri.")