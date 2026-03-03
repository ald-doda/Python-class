import random

n = random.randint(10, 99)

print("Nasumicno generisani dvocifreni broj je:", n,".")

if n % 3 == 0:
    print("Dvocifren broj je djeljiv sa 3.")
else:
    print("Dvocifren broj nije djeljiv sa 3.")