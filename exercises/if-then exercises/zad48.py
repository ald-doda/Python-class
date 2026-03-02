a = float(input("Unesite realan broj: "))

if a < 0:
    apsolutnoA = abs(a)
    print("Racionalan negativan broj je: ", a,".")
    print("Apsolutna vrijednost tog broja je:", apsolutnoA,".")
elif a >= 0:
    print("Broj je pozitivan.")
else:
    print("Greska pri kucanju.")