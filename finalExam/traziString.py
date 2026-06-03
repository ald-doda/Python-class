"""
NapiЕЎite program koji u datom direktorijumu pronalazi datoteku u kojoj se dati string S 
pojavljuje najveД‡i broj puta i ЕЎtampa putanju do te datoteke na konzoli. 
Program treba da primi putanju do direktorijuma i string S koji se traЕѕi u datotekama.
Predavanje 8.5.
"""

import os

direktorijum = input("Unesite putanju do direktorijuma: ")
S = input("Unesite string koji trazite: ")

if not os.path.isdir(direktorijum):
    print("Greska: zadana putanja nije validan direktorijum.")
    exit()

najbolji_fajl = None
max_pojavljivanja = 0

for ime_fajla in os.listdir(direktorijum):
    putanja = os.path.join(direktorijum, ime_fajla)

    if not os.path.isfile(putanja):
        continue

    try:
        with open(putanja, "r", encoding="utf-8") as f:
            sadrzaj = f.read()
        broj = sadrzaj.count(S)
    except Exception:
        continue

    if broj > max_pojavljivanja:
        max_pojavljivanja = broj
        najbolji_fajl = putanja

if najbolji_fajl is None:
    print(f"String '{S}' nije pronadjen ni u jednom fajlu.")
else:
    print(f"Fajl sa najvise pojavljivanja: {najbolji_fajl}")
    print(f"Broj pojavljivanja: {max_pojavljivanja}")
