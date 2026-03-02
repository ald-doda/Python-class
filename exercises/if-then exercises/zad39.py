a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

raz = a - b

if raz > 99 or raz < 1000:
    print("Razlika je trocifrena.")
else:
    print("Razlika nije trocifrena.")
