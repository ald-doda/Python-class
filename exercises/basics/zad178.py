import random

n = random.randint(100, 999)
print("Nasumican broj je: ", n,".")

m = random.randint(100, 999)
print("Nasumican broj  2 je: ", m,".")


d = (n//10)%10

dd = (m//10)%10

sumD = d + dd


print("Suma desetica generisanih brojeva je: ", sumD,".")
