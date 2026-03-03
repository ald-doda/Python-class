import random

n = random.randint(-9, 9)

print("Nasumican broj je", n,".")

if n % 5 != 5:
    print("Broj nije djeljiv sa 5.")
else:
    print("Broj je djeljiv sa 5.")