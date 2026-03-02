a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

raz = a - b

if raz < 10 and raz > -10:
    print("Razlika je jednocifrena")
else:
    print("Razlika je visecifrena.")