#1. Unijeti broj n. U zavisnosti koliki je taj broj, stampaj n redova sa 1,2,3...

#*
#**
#***

n = int(input("Unesite neki broj n: "))
p = "*"

while len(p) <= n:
    print(p)
    p = p + "*"