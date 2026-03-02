import random

n = random.randint(100, 999)
print("Nasumican broj je: ", n,".")

m = random.randint(100, 999)
print("Nasumican broj  2 je: ", m,".")

s = n//100
d = (n//10)%10
j = n%10
sumCifN = s + d + j

ss = n//100
dd = (n//10)%10
jj = n%10
sumCifM = ss + dd + jj

sumCif = sumCifN + sumCifM

print("Suma cifara generisanog broja je: ", sumCif,".")
