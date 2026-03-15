s = "Danas je test"
l = []

for r in s.split():
    l.append(r[::-1])
#a ovdje imamo dodavanje rijeci listi
print(" ".join(l[::-1]))
#join spaja rijeci