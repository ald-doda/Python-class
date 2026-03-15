s = "aaa-bc-cc"

p = s.split("-")
#Odvajamo dje je - i dobijamo listu od 3 rijeci
print(len(p))
print(len(p[0]), len(p[1]))
#Stampa nam koliko karaktera imaju prva i druga rijec
#3 i 2
print(len(set(p[0])),len(set(p[1])))
#Stampa 1 i   jer je jedinsven karakter uz set
