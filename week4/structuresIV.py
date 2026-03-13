#U pythonu postoje i Torke (slicne listama, ali ogranicene)

a = (1,2,3)
b = (1, "PMF", True)

print(b[0]) #Stampa prvi clan b torke odnosno 1
print(b[1]) #Stampa drugi clan b torke odnosno PMF
print(b[0:2]) #Stampa od prvog (0) do zadnjeg clana, bez zadnjeg

#Torke su immutable strukture za razliku od lista
# b[0] = 2 nece raditi

c = a + b
print(c)

#c = a + 4 nece raditi

c = a + (4,) #hoce, dodace se torka
print(c)

print(a.count(2))
print(a.index(3))

#Mozemo definisati i podtorke (kao i podliste)
c = (1, (1, 2, 3, (1, 2, 3)))

b = (2,) + b[1:]
print(b)

#Rjecnici, jako korisni, efikasni, skupovi uredjenih parova
#Jedan clan para je kljuc preko koga se pronalazi druga vrijednost
#Kljuc mora biti jedinstven

imenik = {"Marko" : "063123123", "Bojana" : "067564564", "Andjela" : "069123321"}
print(imenik["Bojana"]) #Stampa broj

imenik["Bojana"] = "067898339"
print(imenik["Bojana"]) #Mijenja broj

imenik["Stefan"] = "066313947"
print(imenik) #Dodaje Stefana unutar

#Kljucne rijeci se  ne mogu promjeniti i brisati
#Marko -> hash funkcija -> 573 (cilj da razliciti stringovi dobiju razlicite vrijednosti)
#Stefan -> 234 (vrijednost se nalazi na poziciji 234)

#Sta moze biti kluc u rjecniku?

svastara = {"pmf": 2, "imenik":{"Kosta": "063456789", "Ana": "063456789"}, "sale":[109, 210]}

#Kljucevi mogu biti samo immutable objekti, npr stringovi, torke, brojevi, klase (liste ne)
mojrecnik = {(1,2) : 5, (3,4) : "Podgorica", 5 : [2,3,4]}
print(mojrecnik[1,2])
#Clear i copy f-je

kopija = svastara.copy()
kopija["pmf"] = 5
print(svastara["pmf"])
kopija["imenik"]["Kosta"] = "063123321"
print(svastara["imenik"]["Kosta"])

print(imenik.get("Andjela"))
#print(imenik["Vladan"]) vraca gresku

print(imenik.get("Vladan")) #Ne vraca gresku vec None(null)
print(imenik.get("Vladan", -1)) #Vraca -1 umesto none

v = imenik.pop("Andjela", None) #Vraca vrijednost, u slucaju da ne postoji vraca None
print(v)

del imenik["Marko"] #Brise Marka
print(imenik)
print("Stefan" in imenik) #Provjerava postoji li kljuc sa imenom stefan
print("Marija" in imenik)

k, v = imenik.popitem() #Izbacuje posljednji par
print(k, v)

imenik.update({"Andjela": "069998319", "Goran" : "891931031"})

#imenik.keys() lista svih kljuceva, .values() svih vrijednosti lista

for key in imenik.keys():
    print(key)

for value in imenik.values(): #Kopije iz rjecnika, ako izmjenis original ostaje isti
    print(value)

for key, value in imenik.items():
    print(key, value)

for key in imenik.keys():
    if imenik[key][0] == "+":
        continue
    imenik[key] = "+382"+imenik[key][1:]

print(imenik)

#Skupovi

skup1 = set([1,2,3,4,5,1,2,3]) #Duplikate ce ponistiti, unutar set se dodaju strukture
print(skup1) #Stampa skupa

print(6 in skup1) #Da li je u skupu, stampa true or false
print(2 in skup1)

skup2 = set([2,4,6,8])

print(skup1 | skup2) #Unija dva skupa
print(skup1 & skup2) #Presjek dva skupa
print(skup1 ^ skup2) #Simetricna razlika, unija  minus presjek

unija = skup1.union(skup2) #Drugi nacin formiranja unije
print(unija)

presjek = skup1.intersection(skup2) #Drugi nacin formiranja presjeka
print(presjek)

simetricna_razlika = skup1.symmetric_difference(skup2) #Drugi nacin predstavljanja simetricne razlike
print(simetricna_razlika)

print(skup1.difference(skup2)) #Elementi koji pripadaju prvom, ali ne i drugom skupu

print(skup1.isdisjoint(skup2)) #Disjunkti - skupovi koji nemaju presjek / provjera - vraca true/false
print(skup1.issubset(skup2)) #Da li je podskup
print(skup1.issubset(unija)) #Da li je podskup

print(skup1.issuperset(skup2)) #Da li je nadskup
skup1.add(6) #Dodati element
print(skup1)

#U skupu su elementi uvijek jedinstevni

skup1.pop() #Izbacuje i vraca prvi element
skup1.remove(4) #Izbacuje dati element, ako ne postoji vraca gresku