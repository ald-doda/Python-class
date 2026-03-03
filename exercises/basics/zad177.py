import random

n = random.randint(10, 99)
m = random.randint(10, 99)

print("Prvi nasumicno generisani trocifreni broj je: ", n,".")
print("Drugi nasumicno generisani trocifreni broj je: ", m,".")

d = n//10
dd = m//10

sum = d + dd

print("Suma cifara desetica dva nasumicno generisana broja je: ", sum,".")