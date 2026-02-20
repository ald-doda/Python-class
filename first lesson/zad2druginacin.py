#isti zadatak kao i zad2.py, ali ovdje unosimo unutar programa, a ne preko inputa.

iznos = 1000 #unosimo iznos kredita
kamata = 3 #unosimo kamatu u procentima
broj_godina = 10 #broj godina nakon kojih zelimo da saznamo iznos
brojac = 1 #brojac koji ce nam pomoci da izracunamo iznos nakon x godina
iznos_kamate = iznos * kamata / 100 #iznos kamate koji se racuna na osnovu formule I = S * K / 100
while(brojac <= broj_godina): #petlja koja se izvrsava dok brojac ne dostigne broj godina
    iznos += iznos_kamate  #dodajemo iznos kamate na iznos kredita
    brojac += 1 #povecavamo brojac za 1 kako bi se petlja izvrsavala tacno broj_godina puta
print("Iznos nakon", broj_godina, "godina je:", iznos) #ispisujemo iznos nakon x godina

'''U ovom nacinu unosimo iznos kredita, kamatu i broj godina unutar programa, 
a zatim racunamo iznos nakon x godina i ispisujemo ga.'''