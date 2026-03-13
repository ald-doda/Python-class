#Kako koristiti f-je/stvari iz drugih skripti

#I nacin:
import math
import structuresIV  #funkcije == structuresIV

print(structuresIV.fun1(5,10)) #Odstampani brojevi - odnosno printovi iz skripte f-je

#U skripti f-je treba napraviti izmjenu da se ne stampa ako se importuje

if __name__ == "__main__":
    print(4)

#II nacin
from structuresIV import fun1, fun2 #Importuje samo odredjene f-je iz druge skripte/biblioteke

#III nacin
import structuresIV as fs #Postaviti kratki alijas za pozive, posto biblioteke obicno imaju dugacke nazive

print(fs.fun1(12,13))

#IV nacin
from structuresIV  import * #Sve importuje kao da je implementirano u trenutnoj skripti
#Ne preporucuje se ovaj nacin jer ne znamo sta ce * sve da ubaci u nas kod ako ubacimo skriptu druge osobe

#Mogu se importovati i druge stvari, npr klase
from classesIV import Automobil