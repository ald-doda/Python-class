import random

n = random.randint(10, 99)
m = random.randint(10, 99)

print("Nasumicno generisani dvocifreni brojevi su: ", n,m,".")

sum = n + m

print("Suma dva broja je ", sum,".")

if sum % 2 != 0:
    print('Suma nije parna.')
else:
    print('Suma je parna.')