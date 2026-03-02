import random

n = random.randint(10, 99)
print("Nasumican broj je: ", n,".")

m = random.randint(10, 99)
print("Nasumican broj  2 je: ", m,".")

d = n//10
j = n%10

dd = m//10
jj = m%10

sabirak1 = d + jj
sabirak2 = dd + j

print("Zadati zbirovi odgovarajucih cifara su: ", sabirak1, sabirak2)
