import random

n = random.randint(1000, 9999)
print("Nasumican broj je: ", n,".")

h = n//1000
s = (n//100)%10
d = (n//10)%10
j = n%10
sumCif = h + s + d + j
print("Suma cifara generisanog broja je: ", sumCif,".")
