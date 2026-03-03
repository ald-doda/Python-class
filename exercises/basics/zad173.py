import random

n = random.randint(1000, 9999)
m = random.randint(1000, 9999)
print("Prvi nasumicno generisani cetvorocifreni broj je: ", n,".")
print("Drugi nasumicno generisani cetvorocifreni broj je: ", m,".")

h = n//1000
s = (n//100)%10
d = (n//10)%10
j = n%10

hh = m//1000
ss = (m//100)%10
dd = (m//10)%10
jj = m%10

sumCifN = h + s + d + j
sumCifM = hh + ss + dd + jj

sumCif = sumCifN + sumCifM 

print("Suma cifara dva nasumicno generisana trocifrena broja je: ", sumCif,".")