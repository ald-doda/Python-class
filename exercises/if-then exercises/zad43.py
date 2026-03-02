ocjena = int(input("Unesite odgovarajucu ocjenu: "))

if ocjena == 5:
    print("Uspjeh je odlican.")
elif ocjena == 4:
    print("Uspjeh je vrlo-dobar.")
elif ocjena == 3:
    print("Uspjeh je dobar.")
elif ocjena == 2:
    print("Uspjeh je dovoljan.")
elif ocjena == 1:
    print("Uspjeh je nedovoljan.")
else:
    print("Greska pri unosu")