import random

n = random.randint(100, 999)
print("Nasumican broj je: ", n,".")

s = n//100
d = (n//10)%10
j = n%10

print("Jedinica nasumicnog broja je: ", j,".")
print("Desetica nasumicnog broja je: ", d,".")
print("Stotina nasumicnog broja je: ", s,".")