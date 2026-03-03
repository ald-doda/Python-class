import random

n = random.randint(10, 99)
m = random.randint(10, 99)
print("Prvi nasumicno generisani dvocifreni broj je: ", n,".")
print("Drugi nasumicno generisani dvocifreni broj je: ", m,".")

d = n//10
j = n%10

dd = m//10
jj = m%10

sumCifN = d + j
sumCifM = dd + jj

sumCif = sumCifN + sumCifM 

print("Suma cifara dva nasumicno generisana dvocifrena broja je: ", sumCif,".")