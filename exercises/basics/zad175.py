import random

n = random.randint(100, 999)
m = random.randint(100, 999)
print("Prvi nasumicno generisani trocifreni broj je: ", n,".")
print("Drugi nasumicno generisani trocifreni broj je: ", m,".")

j = n%10

jj = m%10

sumJ = j + jj

print("Suma jedinica cifara dva nasumicno generisana trocifrena broja je: ", sumJ,".")