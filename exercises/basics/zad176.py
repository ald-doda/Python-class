import random

n = random.randint(1000, 9999)
m = random.randint(1000, 9999)
print("Prvi nasumicno generisani trocifreni broj je: ", n,".")
print("Drugi nasumicno generisani trocifreni broj je: ", m,".")

j = n%10

jj = m%10

sumJ = j + jj

print("Suma jedinica dva nasumicno generisana broja je: ", sumJ,".")