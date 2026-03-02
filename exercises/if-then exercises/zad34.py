a = int(input("Unesite vrijednost broja a: "))
b = int(input("Unesite vrijednost broja b: "))

raz = a - b

if raz > 10 or raz < -10:
    print("Razlika je dvocifrena.")
else:
    print("Razlika nije dvocifrena.")