import random

n = random.randint(10, 99)

print("Nasumicno generisan dvocifren broj je ", n,".")

if n % 2 != 0:
    print("Dvocifren broj nije paran.")
else:
    print("Dvocifren broj je paran.")