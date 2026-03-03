import random

n = random.randint(100, 999)
m = random.randint(100, 999)
print("Prvi nasumicno generisani trocifreni broj je: ", n,".")
print("Drugi nasumicno generisani trocifreni broj je: ", m,".")
s = n//100
d = (n//10)%10
j = n%10

ss = m//100
dd = (m//10)%10
jj = m%10

sumCifN = s + d + j
sumCifM = ss + dd + jj

sumCif = sumCifN + sumCifM 

print("Suma cifara dva nasumicno generisana trocifrena broja je: ", sumCif,".")