#3. Za n=3 istampati ovakav oblik:

#   *
#  ***
# *****
#  ***
#   *

n = int(input("Unesite vrijednost n: "))
p = "*"

while len(p) <= n:
    print(" " * ((n - len(p)) // 2) + p)
    p = p + "**"

p = p[:-2]

while len(p)>= 1:
    print(" " * ((n - len(p)) // 2) + p)
    p = p[:-2]
