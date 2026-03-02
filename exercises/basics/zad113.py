n = int(input("Unesite vrijednost trocifrenog broja n: "))

s = n//100
d = (n//10)%10
j = n%10

sumCif = s + d + j

print("Suma cifara su: ", sumCif,".")