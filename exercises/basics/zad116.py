n = int(input("Unesite vrijednost petocifrenog broja n: "))

dH = n//10000
h = (n//1000)%10
s = (n//100)%10
d = (n//10)%10
j = n%10


print("Cifre su: ", dH,h,s,d,j,".")