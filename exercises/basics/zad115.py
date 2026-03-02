n = int(input("Unesite vrijednost cetvorocifrenog broja n: "))

h = n//1000
s = (n//100)%10
d = (n//10)%10
j = n%10


print("Cifre su: ", j,d,s,h,".")