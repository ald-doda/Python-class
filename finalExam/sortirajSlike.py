"""
Napisati program koji u datom direktorijumu kreira tri poddirektorijuma sa nazivima 
"Slike JPG", "Slike PNG" i "Slike GIF", a zatim pronalazi sve slike u tom direktorijumu 
(datoteke sa ekstenzijama .jpg, .png i .gif) i premjeЕЎta ih u odgovarajuД‡i poddirektorijum 
(.jpg u poddirektorijum "Slike JPG", .png u poddirektorijum "Slike PNG" i .gif u poddirektorijum "Slike GIF"). 
Sve ostale datoteke u datom direktorijumu program treba da obriЕЎe. 
Putanju do direktorijuma moЕѕete definisati direktno u programu ili omoguД‡iti korisniku da je unese.
Predavanje 8.5.
"""
import os
import shutil

direktorijum = input("Unesite putanju do direktorijuma: ")

if not os.path.isdir(direktorijum):
    print("GreЕЎka: zadana putanja nije validan direktorijum.")
    exit()

folderi = {
    ".jpg": "Slike JPG",
    ".png": "Slike PNG",
    ".gif": "Slike GIF",
}

for naziv in folderi.values():
    os.makedirs(os.path.join(direktorijum, naziv), exist_ok=True)

for ime_fajla in os.listdir(direktorijum):
    putanja = os.path.join(direktorijum, ime_fajla)

    if not os.path.isfile(putanja):
        continue

    ekstenzija = os.path.splitext(ime_fajla)[1].lower()

    if ekstenzija in folderi:
        odrediste = os.path.join(direktorijum, folderi[ekstenzija], ime_fajla)
        shutil.move(putanja, odrediste)
        print(f"Premjesten: {ime_fajla} -> {folderi[ekstenzija]}/")
    else:
        os.remove(putanja)
        print(f"Obrisan:    {ime_fajla}")

print("Kraj.")
