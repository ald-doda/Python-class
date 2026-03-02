from math import sqrt

a = int(input("Unesite vrijednosti a: "))
b = int(input("Unesite vrijednosti b: "))
c = int(input("Unesite vrijednosti c: "))

obim = a + b + c
poluobim = obim/2
povrsina = sqrt(poluobim*(poluobim-a)*(poluobim-b)*(poluobim-c))

print("Povrsina je jednaka: ", povrsina,".")