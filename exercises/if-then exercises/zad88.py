import random

n = random.randint(10, 99)

print("Nasumicno generisani dvocifreni broj je", n,".")

if n % 2 == 0:
    print("Dvocifren broj je djeljiv sa 2.")
else:
    print("Broj nije djeljiv sa 2.")