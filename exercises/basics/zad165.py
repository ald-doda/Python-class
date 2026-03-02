import random

n = random.randint(1000, 9999)
print("Nasumican broj je: ", n,".")

h = n//1000
s = (n//100)%10
d = (n//10)%10
j = n%10

print("Hiljada nasumicnog broja je: ", h,".")
print("Stotina nasumicnog broja je: ", s,".")
print("Desetica nasumicnog broja je: ", d,".")
print("Jedinica nasumicnog broja je: ", j,".")