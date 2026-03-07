#Treci cas

#I lista

a = [2, 3, 4, 5, 6]

#II lista

b = [ 2, 3.24, "pmf", [2, 3, 4]]

#Isto kao sa stringovima, i sa listama mozemo da pristupamo pojedinacnim elementima preko indeksa

print(a[1])     #indeksiranje krece od 0 tako da ce da se istampa 3
print(b[2])     #indeksiranje krece od 0 tako da ce da se istampa "pmf"
#Mozemo da pristupamo i djelovima liste, slicno kao sa stringovima

print(a[1:3])  #3 i 4 se stampa --> zadnji se ne stampa
print(a[-2])    #drugi od pozadi --> 5

print(a[::2])   #svi elementi sa parnim indeksom --> 2, 4, 6

print(a[:3])    #prva 3 elementa --> 2, 3, 4

print(a[3:1:-1])   #od 3 do 1 unazad --> 5, 4

c = a + b   #nadovezivanje dvije liste

print(c)    #sve elemente iz a i b ce da nadoveze u novu listu c

d = a * 3   #3 puta ce da nadoveze listu samom sebi

print(d)    #2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6

e = [0] * 10   #kreira listu od 10 elemenata, gdje je svaki element 0

a [1:3] = [11, 12]   #od 1 do 3 ce novi elementi da budu --> 3 i 4 ce da postanu 11 i 12
a [1:3] = [20, 21, 22]   #ne mora da se poklopi duzina --> 11 i 12 ce da postanu 20, 21, 22
a [1:3] = []   #a nismo morali da stavimo ni jedan broj --> jedan od nacina za brisanje el. iz liste --> 20, 21, 22 ce da se obrisu

#Funkcije koje se mogu koristiti nad listama:

print(len(a))   #duzina liste a, stampa 4

g = list("python")   #kreira listu od stringa, svaki karakter ce biti poseban element

print(g)    #stampa ['p', 'y', 't', 'h', 'o', 'n']

#For petlja nad listama:

for el in a:

    print(el + 5) #stampa svaki element iz liste a uvecan za 5

for el in a:

    if el % 2 == 0:

        continue    #ako je element paran, preskoci ga i nastavi dalje
    
    print(el)
else:
    
        print("Izvrsava se ako nije bilo break-a")

for c in "pmf podgorica":
     
     print(c) #stampa svaki karakter iz stringa "pmf podgorica" u novom redu

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #kreira listu od 1 do 10

for el in a:
     
     el = el + 1 #uvecava svaki element za 1, ali ne mijenja element u listi a


for ind, el in enumerate(a): #enumerate vraca indeks i element, ind je indeks a el je element / pravi listu parova (indeks, element)

     a[ind] = a[ind] + 1 #uvecava element na indeksu ind za 1, mijenja element u listi a

print(a) #stampa listu a nakon izmjene, svaki element ce biti uvecan za 1, stampa [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

a.append(28) #dodaje element 28 na kraj liste a

a.clear(a) #brisanje svih elemenata iz liste a, lista a ce postati prazna

b = a.copy(a) #kopira listu a u novu listu b, b ce biti prazna lista jer je a prazna

b = a #shallow copy - plitka kopija

print(a[0])

b[0] = 7 #ako promijenimo element na indeksu 0 u listi b, promijenice se i u listi a jer su a i b reference na istu listu

print(a[0]) #stampa 7, jer je element na indeksu 0 u listi a promijenjen preko liste b


b = a.copy() #deep copy - duboka kopija

b[0] = 10 #ako promijenimo element na indeksu 0 u listi b, nece se promijeniti u listi a jer su a i b sada dvije odvojene liste

print(a[0]) #stampa 7, jer je element na indeksu 0 u listi a ostao nepromijenjen

a = [2, 3, 4, [1, 2, 3,]]

b = a.copy() #shallow copy - plitka kopija

print(a[3][0]) #stampa 1, element na indeksu 3 u listi a je lista [1, 2, 3], a element na indeksu 0 u toj listi je 1

b[3][0] = 19 #ako promijenimo element na indeksu 0 u listi na indeksu 3 u listi b, promijenice se i u listi a jer su a i b reference na istu listu, a element na indeksu 3 je lista koja je referencirana

print(a[3][0]) #stampa 19, jer je element na indeksu 0 u listi na indeksu 3 u listi a promijenjen preko liste b

a = [1, 2, 3, 2, 3, 2, 2]

print(a.count(2)) #stampa koliko puta se element 2 pojavljuje u listi a, stampa 5

a.extend([4, 5, 5, 4, 5, 7, 2]) #nadovezuje listu

print(a) #stampa listu a nakon nadovezivanja, stampa [1, 2, 3, 2, 3, 2, 2, 4, 5, 5, 4, 5, 7, 2]

print(a.index(4)) #stampa indeks prvog pojavljivanja elementa 4 u listi a, stampa 7

if 0 in a:
     
     print(a.index(0)) #ako je element 0 u listi a, stampa indeks prvog pojavljivanja elementa 0, ali element 0 nije u listi a, pa se nece nista stampati

print(5 in a) #True, element 5 je u listi a

print(3 in a) #False, element 3 nije u listi a


a.index(4, 8) #trazimo 4 od 8. indexa pa nadalje
a.index(4, 5, 10) #trazimo 4 od 5. indexa do 10. indexa (ne ukljucujuci 10. index)

a = [1, 2, 3, 4, 5]

a.insert(0, 6) #Na poziciji nula se dodaje 6
#Lista ce postati [6, 1, 2, 3, 4, 5]

a.insert(2, 10) #Na poziciji 2 se dodaje 10
#Lista ce postati [6, 1, 10, 2, 3, 4, 5]

a.pop(0) #Brise element na poziciji 0, a to je 6
#Lista ce postati [1, 10, 2, 3, 4, 5]

a.remove(10) #Brise prvi element koji je jednak 10, a to je element na poziciji 1
#Lista ce postati [1, 2, 3, 4, 5]

b = [1, 2, 2, 3, 4, 3, 2, 3, 2]

#Kako da svako pojavljivanje izbacimo:

for el in b:
     
     if el == 3:
          
          b.remove(el) #ako je element jednak 3, izbacujemo ga iz liste b, ali ovo ce da izbacuje samo prvo pojavljivanje broja 3, a ne svako pojavljivanje broja 3, jer se lista mijenja tokom iteracije, pa se neki elementi preskacu


while 3 in b:
     
     b.remove(3) #ako je element 3 u listi b, izbacujemo ga iz liste b, ovo ce da izbacuje svako pojavljivanje broja 3, jer se lista mijenja tokom iteracije, ali se ne iterira preko liste, vec se samo provjerava da li je broj 3 u listi b i ako jeste, izbacuje se, i ponavlja se dok god je broj 3 u listi b

print(b) #stampa listu b nakon izbacivanja svih pojavljivanja broja 3, stampa [1, 2, 2, 4, 2, 2]

b.reverse() #obrnuto redoslijed elemenata u listi b


print(b) #stampa listu b nakon obrnutog redoslijeda, stampa [2, 2, 4, 2, 2, 1]

c = [3, 4, 1, 5, 2, 1]

c.sort() #sortira elemente u listi c u rastucem redoslijedu

print(c) #stampa listu c nakon sortiranja, stampa [1, 1, 2, 3, 4, 5]


d = ["Marija", "Goran", "Marko", "Ana"]

d.sort() #sortira elemente u listi d po abecednom redu

print(d) #stampa listu d nakon sortiranja, stampa ['Ana', 'Goran', 'Marija', 'Marko']

d.sort(reverse=True) #sortira elemente u listi d po obrnutom abecednom redu

print(d) #stampa listu d nakon sortiranja po obrnutom abecednom redu, stampa ['Marko', 'Marija', 'Goran', 'Ana']

#SORT ce da bude na kolokvijumu 100%

c.sort(reverse=True) #sortira elemente u listi c po obrnutom redoslijedu
print(c) #stampa listu c nakon sortiranja po obrnutom redoslijedu, stampa [5, 4, 3, 2, 1, 1]

def duzina(x):
        return len(x) #funkcija koja vraca duzinu argumenta x
   #ovdje mozemo return -len(x) "MINUS"


d.sort(key=duzina) #sortira elemente u listi d po duzini stringa, od najkraceg do najduzeg

d.sort(key=duzina, reverse=True) #sortira elemente u listi d po duzini stringa, od najduzeg do najkraceg

def moje_poredjenje(x):
     
     return x % 2 #funkcija koja vraca ostatak pri dijeljenju x sa 2, ovo ce da sortira elemente u listi c tako da ce parni brojevi biti prije neparnih brojeva, jer ce parni brojevi imati ostatak 0, a neparni brojevi ce imati ostatak 1


c.sort(key=moje_poredjenje) #sortira elemente u listi c tako da ce parni brojevi biti prije neparnih brojeva

print(c) #stampa listu c nakon sortiranja po funkciji moje_poredjenje, stampa [4, 2, 1, 1, 5, 3] - parni brojevi su prije neparnih brojeva

def moje_poredjenje(x):
     
     return x % 2, x % 3
#funkcija koja vraca (x % 2, x % 3), ovo ce da sortira elemente u listi c prvo po parnosti, a zatim po ostatku pri dijeljenju sa 3, tako da ce parni brojevi biti prije neparnih brojeva, a unutar parnih brojeva ce biti sortirani po ostatku pri dijeljenju sa 3, a unutar neparnih brojeva ce biti sortirani po ostatku pri dijeljenju sa 
