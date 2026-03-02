import random

n = random.randint(1000, 9999)
print("Nasumican broj je: ", n,".")

m = random.randint(1000, 9999)
print("Nasumican broj  2 je: ", m,".")

s = (n//100)%10
ss = (m//100)%10

sumS = s + ss

print("Suma stotina generisanih brojeva je: ", sumS,".")
