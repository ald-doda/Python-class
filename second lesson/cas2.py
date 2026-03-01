#Stringovi

#Stringovi u Pythonu se mogu definisati na vise nacina:

s1 = "programiranje" #mogu se navesti uz duple navodnike
s2 = 'python' #kao i uz jednostruke navodnike

#Mozemo pristupati karakterima unutar stringa, kao i samim stringovima

print(s1[0]) #ovdje nam ucitava samo prvi karakter datog stringa
print(type(s1[0])) #ovdje nam govori o tipu datog stringa

#Unutar pravougle zagrade se moze navesti samo jedan broj

#U slucaju da zelimo uzeti vise stringova iz neke klase, to radimo na sljedeci nacin:
print(s1[0:3]) #Ovdje uzimamo sve stringove iz klase od 0 do 3
#Na kolokvijumu ce biti makar jedan zadatak slican ovome

print(s1[:5]) #U ovom slucaju se stampa prvih 5 karaktera.

print(s1[1:8:2]) 

print(s1[::3]) #U ovom slucaju se stampa svaki treci karakter
print(s1[::]) #U ovom slucaju se stampa cijela rijec

s3: str=s1[::]

print(s1[-1]) #U ovom slucaju se stampa zadnji karakter

print(s1[-2]) #U ovom slucaju se stampa predzadnji karakter

print(s1[-5:-1]) #U ovom slucaju se stampa od petog do predzadnjeg

print(s1[::-1]) #U ovom slucaju se sve ispisuje unazad

#s1[0] = c

s3 = s1 + s2 #Operacija sabiranja
print(s3) #Spajaju se dva stringa u jedan

s4= s1*3 #Moguce je pomnoziti string brojem
print(s4) #Ispisivanje stringa koji je proizvod

z5 = 'P' + s1[1:] #U ovom slucaju mozemo ispraviti malo u veliko slovo
print(z5) #Ispisivanje stringa sa velikim pocetnim slovom

#Funkcije sa strinovima
print(len(s1)) #Ispisivanje duzine stringa
#Takodje se len moze upotrebiti za ispisivanje neceg drugog

#Pretvaranje nekog drugog tipa podatka u string:

a=3.14
a = str(a)
print(a*5)

#Funkcije pocinju sa tackom

s5= "PMF Podgorica"
s5 = s5.capitalize
print(s5)

s6 = "programiranje".upper() #Pretvara sve karaktere u velika slova
print(s6) #Ispisivanje svih velikih karaktera

s7 = "PMF Podgorica".lower() #Pretvaranje svih karaktera u mala slova
print(s7) #Ispisivanje svih malih karaktera

s8 = " Programiranje "
print(s8.count("a")) #Broji koliko karaktera a imamo u stringu
#Moze brojati i vise slova/karaktera
print(s8.count("ra")) #Broji koliko ra ima u stringu
print(s8.count("ra", 3, 7)) #Izmedju treceg i sedmog karaktera koliko ra ima

print(s8.index("a"))
print(s8.index("ra"))
print(s8.index("ra", -7, -3))

print(s8.find("h"))
print(s8.find("ra", 3, 7))
print(s8.find("ra", -3, -7))

print(s8.rfind("ra")) #rfind i rindex posljednje pojavljivanje ili posljednji indeks

s9 = "                  programiranje  "
s9 = s9.strip() #Strip brise bjelinu iz teksta
print(s9)

#Lstrip brise bjeline samo sa lijeve strane
#Rstrip brise bjeline sa desne strane

#Replace sluzi za promjenu stringa nekim drugim stringom

s8 = s8.replace("ra", "RA")
print(s8)
#Karakteri ra su postali RA

s10 = s8.replace("ra", "")
print(s10) #Ovdje brisemo ra

#Mozemo zapisati i koliko puta pravimo zamjenu
s10 = s8.replace("ra", "", 1)
print(s10)

#Mozemo vidjeti da li se karakter sastoji samo od slova ili brojeva
print("dhadahshakdash12".isalnum())
print("2d389h280fw0iedjssd.".isalnum())
#Da li se sastoji samo od slova?
print("jafdjsnfdsjndsknsd".isalpha())
print("jmcdsomcskdc9".isalpha())

#Provjerava da li se string sastoji samo od cifara?
print("9320238239".isdecimal())
print("230984234843734sksd".isdecimal())
#Da li je string numericki, razliku ne znamo??
print("0xa".isdecimal())
print("0xa".isnumeric())

#Imamo isupper koji provjerava jesu li sva slova velika?
print("PMF".isupper())
#Ako ima brojeva i/ili malih slova pise false
#Slicno i za islower
print("jfjfkof".islower())

