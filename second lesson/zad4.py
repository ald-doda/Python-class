#4. Provjeravamo da li je sifra validna
#Treba da vazi - barem  6 karaktera, jedno veliko i malo slovo.
#Kao i jednu cifru i jedan specijalan karakter.

sifra = input("Unesite sifru: ")

if len(sifra) < 6 :
    print("Sifra mora imati makar 6 karaktera.")

maloSlovo = False
velikoSlovo = False
broj = False
specijalniKarakter = False

i = 0

while i < len(sifra):
    if sifra[i].isupper():
        velikoSlovo = True
    elif sifra[i].islower():
        maloSlovo = True
    elif sifra[i].isdigit():
        broj = True
    else:
        specijalniKarakter = True
    i +=1

if len(sifra) >= 6 and velikoSlovo == True and maloSlovo == True and specijalniKarakter == True:
    print("Sifra je validna.")
else:
    print("Sifra nije validna.")