import os
import shutil
#Predavanje 8.5.
# 1. KREIRANJE FOLDERA
os.mkdir("moj_folder")  # puca ako folder vec postoji
print("Kreiran folder: moj_folder")

# os.mkdir("moj_folder")  # puca ako folder vec postoji
os.mkdir("moj_folder", exist_ok=True)  # ne puca ako folder vec postoji

os.makedirs("moj_folder/podaci/rezultati", exist_ok=True)
print("Kreirana putanja: moj_folder/podaci/rezultati")

# 2. KREIRANJE I PISANJE U FAJL
# "w" = write (kreira novi ili poniЕЎtava sadrЕѕaj postojeД‡eg fajla)

# BEZ with (stariji naДЌin)
# Fajl se mora ruДЌno zatvoriti pomoД‡u f.close(), inaДЌe ostaje otvoren u memoriji
f = open("moj_folder/pozdrav.txt", "w", encoding="utf-8")
f.write("Zdravo, svima!\n")
f.write("Ovo je moj prvi fajl.\n")
f.close()

# SA with (preporuДЌeni naДЌin)
# "with" automatski zatvara fajl ДЌim se izaД‘e iz bloka (ДЌak i ako doД‘e do greЕЎke)
# "as f" znaДЌi: otvoreni fajl dodijeli varijabli f, da moЕѕemo pisati f.write(...)
with open("moj_folder/pozdrav.txt", "w", encoding="utf-8") as f:
    f.write("Zdravo, svima!\n")
    f.write("Ovo je moj prvi fajl.\n")

print("Fajl 'pozdrav.txt' kreiran i upisan.")

# Dodavanje na kraj fajla bez brisanja sadrЕѕaja - "a" = append
with open("moj_folder/pozdrav.txt", "a", encoding="utf-8") as f:
    f.write("Ovo je dodato naknadno.\n")

print("Dodata nova linija u 'pozdrav.txt'.")


# 3. ДЊITANJE IZ FAJLA
# ДЊitanje cijelog sadrЕѕaja odjednom
with open("moj_folder/pozdrav.txt", "r", encoding="utf-8") as f:
    sadrzaj = f.read()

print("Cijeli sadrzaj fajla:")
print(sadrzaj)

# ДЊitanje liniju po liniju
print("Linija po linija:")
with open("moj_folder/pozdrav.txt", "r", encoding="utf-8") as f:
    for broj, linija in enumerate(f, start=1):
        print(f"  Linija {broj}: {linija.strip()}")


# 4. PROVJERA DA LI FAJL/FOLDER POSTOJI
print(f"Postoji li 'moj_folder'?       {os.path.exists('moj_folder')}")
print(f"Postoji li 'pozdrav.txt'?      {os.path.exists('moj_folder/pozdrav.txt')}")
print(f"Postoji li 'nepostojeci.txt'?  {os.path.exists('nepostojeci.txt')}")
print(f"Je li 'moj_folder' folder?     {os.path.isdir('moj_folder')}")
print(f"Je li 'pozdrav.txt' fajl?      {os.path.isfile('moj_folder/pozdrav.txt')}")


# 5. LISTANJE SADRZAJA FOLDERA
stavke = os.listdir("moj_folder")
print(f"Sta se nalazi u 'moj_folder': {stavke}")

# Detaljnije - razlikujemo fajlove od foldera
print("\nDetaljno:")
for stavka in os.listdir("moj_folder"):
    # join spaja dijelove putanje ispravno bez obzira na OS (/ ili \)
    puna_putanja = os.path.join("moj_folder", stavka)
    tip = "FOLDER" if os.path.isdir(puna_putanja) else "FAJL"
    print(f"  [{tip}] {stavka}")


# 6. RAD SA PUTANJAMA
putanja = "moj_folder/pozdrav.txt"
print(f"Puna putanja:    {os.path.abspath(putanja)}")
print(f"Samo ime fajla:  {os.path.basename(putanja)}")
print(f"Samo folder:     {os.path.dirname(putanja)}")

ime, ekstenzija = os.path.splitext(os.path.basename(putanja))  # split razdvaja na ime i ekstenziju
print(f"Ime bez ext.:    {ime}")
print(f"Ekstenzija:      {ekstenzija}")

# 7. KOPIRANJE I PREMJESTANJE
# Kopiranje fajla
shutil.copy("moj_folder/pozdrav.txt", "moj_folder/pozdrav_kopija.txt")
print("Kopiran fajl: pozdrav.txt -> pozdrav_kopija.txt")

# PremjeЕЎtanje / preimenovanje
os.rename("moj_folder/pozdrav_kopija.txt", "moj_folder/podaci/arhiva.txt")
print("PremjeЕЎten/preimenovan fajl u: podaci/arhiva.txt")


# 8. VELICINA I INFO O FAJLU
velicina = os.path.getsize("moj_folder/pozdrav.txt")
print(f"VeliДЌina 'pozdrav.txt': {velicina} bajtova")


# 9. BRISANJE
# Brisanje jednog fajla
os.remove("moj_folder/podaci/arhiva.txt")
print("Obrisan fajl: podaci/arhiva.txt")

# Brisanje praznog foldera
os.rmdir("moj_folder/podaci/rezultati")
print("Obrisan prazan folder: podaci/rezultati")

# Brisanje foldera sa svim sadrzajem unutra
shutil.rmtree("moj_folder")
print("Obrisan cijeli folder 'moj_folder' sa svim sadrЕѕajem.")
