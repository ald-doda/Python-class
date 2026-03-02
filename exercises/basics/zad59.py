brojac = 0
suma = 0

while brojac<5:
    ocjena = int(input("Unesite ocjenu: "))
    suma = suma + ocjena
    brojac = brojac + 1

prosjek = suma / 5.0

print("Prosjek je", prosjek,".")