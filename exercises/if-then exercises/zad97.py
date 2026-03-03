import random

n = random.randint(10, 99)
m = random.randint(10, 99)

print("Nasumicno generisani dvocifreni brojevi su: ", n,m,".")
if n % m != 0:
    print('Prvi broj nije djeljiv sa drugim.')
else:
    print('Prvi broj je djeljiv sa drugim.')