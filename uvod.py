#Uvod u Python

#Inicijalizacija i dodjeljivanje vrijednosti varijablama
a = 5
b, c, d = 1, 2, 3 #Ne mora se stavljati tackka-zarez na kraju linije

#Aritmeticki operatori
print(a+b) #sabiranje
print(a-b) #oduzimanje
print(a*b) #mnozenje
print(a/b) #dijeljenje
print(a//b) #cijelobrojno dijeljenje
print(a%b) #dobijanje ostatka pri dijeljenju
print(b**c) #stepenovanje b^c
print(a**b) #stepenovanje a^b

#Logicki operatori
a = True #logicka vrijednost True (istina)
b = False #logicka vrijednost False (neistina)
print(a and b) #logicko i
print(a or b) #logicko ili
print(not a) #logicko ne
print(not b) #logicko ne

#Pretvaranje tipova podataka

#pretvaranje float-a u int, int-a u string
f = 3.14 #float (decimalni broj)
g = int(f) #pretvaranje float-a u int (cijeli broj) - g ce biti 3, decimalni dio se odbacuje
print(f, g) #ispis f i g, f ce biti 3.14, a g ce biti 3
h = str(g) #pretvaranje int-a u string (tekst) - h ce biti "3"
print(h) #ispis h, h ce biti "3"

#Pretvaranje brojeva u binarni, heksadecimalni i oktalni zapis

#binarni zapis
a = 0b1001 #binarni zapis broja 9 
b = 0b11  #binarni zapis broja 3 
print(a*b) #mnozenje binarnih brojeva, rezultat ce biti 27 (9*3)

#heksadecimalni zapis
c= 0xab #heksadecimalni zapis broja 171
d = 0x1f #heksadecimalni zapis broja 31
print(c+d) #sabiranje heksadecimalnih brojeva, rezultat ce biti 202 (171+31)

#oktalni zapis
h = 0o123 #oktalni zapis broja 83
i = 0o77 #oktalni zapis broja 63
print(h-i) #oduzimanje oktalnih brojeva, rezultat ce biti 20 (83-63)

#Operatori uporedjivanja
a = 5 #inicijalizacija varijable a sa vrijednosti 5
b = 10 #inicijalizacija varijable b sa vrijednosti 10
print(a == b) #provjera jednakosti
print(a != b) #provjera nejednakosti
print(a > b) #provjera veceg
print(a < b) #provjera manjeg
print(a >= b) #provjera veceg ili jednakog
print(a <= b) #provjera manjeg ili jednakog

#Unos podataka od korisnika i konverzija tipova
a= input("Unesite neki broj: ") #unos broja od korisnika, rezultat ce biti string (tekst)
print(a*5) #ispis unesenog broja pomnozenog sa 5 (ali kao string)
a = int(a) #pretvaranje unesenog stringa u int (cijeli broj)
print(a*5) #ispis unesenog broja pomnozenog sa 5 (sada kao int)

#ili sve u jednoj liniji
a=int(input("Unesite neki broj: ")) #unos broja od korisnika i pretvaranje u int
print(a*5) #ispis unesenog broja pomnozenog sa 5 (sada kao int)

#Uslovne naredbe (if-elif-else)

#if-elif-else struktura
if(a>10): #provjera da li je a vece od 10
    print("Uneseni broj je veci od 10") #ako je uslov zadovoljen, izvrsava se ovaj kod
elif(a==10): #ako prethodni uslov nije zadovoljen, provjerava se ovaj uslov
    print("Uneseni broj je jednak 10") #ako je ovaj uslov zadovoljen, izvrsava se ovaj kod
else: #ako nijedan od prethodna dva uslova nije zadovoljen, izvrsava se ovaj kod
    print("Uneseni broj je manji od 10") #ako nije uslov zadovoljen, izvrsava se ovaj kod

#if-elif-else struktura sa vise uslova
if(a>10): #provjera da li je a vece od 10
    print("Uslov je zadovoljen") #ako je uslov zadovoljen, izvrsava se ovaj kod
    print("Jos jedna naredba") #ako je uslov zadovoljen, izvrsava se i ova naredba (ako je uvucena)
elif(a>7): #ako prethodni uslov nije zadovoljen, provjerava se ovaj uslov
    print("Drugi uslov je zadovoljen") #ako je ovaj uslov zadovoljen, izvrsava se ovaj kod
elif(a>6): #ako prethodni uslov nije zadovoljen, provjerava se ovaj uslov
    print("Treci uslov je zadovoljen") #ako je ovaj uslov zadovoljen, izvrsava se ovaj kod
else: #ako nijedan od prethodna tri uslova nije zadovoljen, izvrsava se ovaj kod
    print("Uslov nije zadovoljen") #ako nije uslov zadovoljen, izvrsava se ovaj kod

#ako imamo if-ove sa else if-ovima kada se zadovolji neki uslov, ostali se ne provjeravaju
#if zasebno, svi se provjeravaju bez obzira na to da li je neki

#vise if-ova bez else if-ova, svi se provjeravaju bez obzira na to da li je neki uslov zadovoljen
if(a>10): #provjera da li je a vece od 10
    print("Uslov je zadovoljen") #ako je uslov zadovoljen, izvrsava se ovaj kod
    print("Jos jedna naredba") #ako je uslov zadovoljen, izvrsava se i ova naredba (ako je uvucena)
if(a>7): #ako prethodni uslov nije zadovoljen, provjerava se ovaj uslov
    print("Drugi uslov je zadovoljen") #ako je ovaj uslov zadovoljen, izvrsava se ovaj kod
if(a>6): #ako prethodni uslov nije zadovoljen, provjerava se ovaj uslov
    print("Treci uslov je zadovoljen") #ako je ovaj uslov zadovoljen, izvrsava se ovaj kod
else: #ako nijedan od prethodna tri uslova nije zadovoljen, izvrsava se ovaj kod
    print("Uslov nije zadovoljen") #ako uslov nije zadovoljen, izvrsava se ovaj kod

#Petlje (while i for)

#while petlja
i=0 #inicijalizacija brojača i sa vrijednosti 0
while(i<10): #uslov petlje, petlja ce se izvrsavati sve dok je i manje od 10
    print(i) #ispisujemo i prije povecanja da bi se vidjelo da i pocinje od 0
    i+=1 #povecanje brojača i za 1 (i = i + 1)
    print(i) #ispisujemo i nakon povecanja da bi se vidjelo da i se povecava za 1 svaki put

while(i<10): #uslov petlje, petlja ce se izvrsavati sve dok je i manje od 10
    if(i%2==0): #provjera da li je i paran broj
        print(i) #ispis parnih brojeva
    else: #ako nije paran, onda je neparan
        print(i) #ispis neparnih brojeva

#for petlja
for i in range(10): #for petlja koja ce se izvrsavati 10 puta, i ce uzimati vrijednosti od 0 do 9
    if(i%2==0): #provjera da li je i paran broj
        print(i) #ispis parnih brojeva
    else: #ako nije paran, onda je neparan
        print(i) #ispis neparnih brojeva

#break i continue
    if(i==5): #ako i dostigne vrijednost 5, prekida se petlja
        break #prekidanje petlje kada i dostigne 5
    print(i) #ispis i, ali se nece ispisati 5 jer se petlja prekida kada i dostigne 5

    if(i==5):
        continue #preskakanje ostatka koda u petlji kada i dostigne 5, i se nece ispisati
    print(i) #ispis i, ali se nece ispisati 5 jer se kada i dostigne 5 preskace ostatak koda u petlji
