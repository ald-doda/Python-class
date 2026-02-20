#dat je iznos kredita S i kamata u procentima K. 
# Kamata se obračunava na osnovu formule: I = S * K / 100. 
# Napisati program koji učitava iznos kredita i kamatu, računa i ispisuje iznos kamate. 
# Koliki ce biti iznos nakon x godina?

S = float(input("Unesite iznos kredita: ")) #iznos kredita S
K = float(input("Unesite kamatu u procentima: ")) #kamata K
I = S * K / 100  #iznos kamate I uz formulu I = S * K / 100
print("Iznos kamate je:", I) #ispis iznosa kamate
x = int(input("Unesite broj godina: ")) #unos broja godina x
iznos_nakon_x_godina = S + I * x #iznos nakon x godina formula S + I * x
print("Iznos nakon", x, "godina je:", iznos_nakon_x_godina) #ispis iznosa nakon x godina

'''U ovom nacinu unosimo iznos kredita, kamatu i broj godina, a zatim racunamo iznos nakon x godina i ispisujemo ga.'''