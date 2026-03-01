#2. Po istom principu kao i prvi zadatak, samo je sada cilj ici i od n nazad ka 1.

#*
#**
#***
#****
#***
#**
#*

n = int(input("Unesite vrijednost n: "))
p = "*"

while len(p) <= n:
    print(p)
    p = p + "*"

p = p[:-1]

while len(p) > 1:
    print(p[:-1])
    p = p[:-1]


