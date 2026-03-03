import random

n = random.randint(10, 99)

print("Nasumicno generisani dvocifreni broj je:", n,".")

if n % 5 != 0:
    print("Dvocifren broj je djeljiv sa 5.")
else:
    print("Dvocifren broj nije djeljiv sa 5.")