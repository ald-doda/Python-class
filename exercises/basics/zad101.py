n = int(input("Unesite vrijednosti trocifrenog broja n: "))

cDsS = n//100
cDsD = n//10

oSs = n%100
oSd = n%10

print("Cjelobrojno djeljenje sa 100 i 10 daje rezultate:", cDsS, cDsD,"a ostatak djeljenja sa 100 i 10 daje rezultate:", oSs, oSd,".")