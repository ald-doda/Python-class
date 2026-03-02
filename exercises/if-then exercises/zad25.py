a = int(input('Unesite vrijednost broja a: '))

if a == 0:
    print("Nedefinisan izraz.")
elif a != 0:
    recVr = 1/a
    print("Reciprocna vrijednost je: ", recVr)
else:
    print("Greska")
