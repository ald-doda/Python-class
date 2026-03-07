def fun1(a, b): #definicija funkcije fun1 koja prima dva argumenta a i b

    s = a + b #sabira a i b i smjesta rezultat u varijablu s

    return s #vraca vrijednost s, a to je zbir a i b

print(fun1(10, 17))     #pozivamo funkciju fun1 sa argumentima 10 i 17, i stampa se rezultat, a to je 27


def fun2(a, b = 5, c = 10): #poslije prvog elementa se sa podrazumijevanom vrijednoscu svi moraju da ih imaju, funkcija fun2 prima tri argumenta a, b i c, gdje b i c imaju podrazumijevane vrijednosti 5 i 10

    '''

    Ova funkcija sabira 3 broja.

    a - prvi broj

    b - drugi broj

    c - treci broj

    '''

    

    return a + b + c #vraca zbir a, b i c

print(fun2(9)) #pozivamo funkciju fun2 sa argumentom 9, i stampa se rezultat, a to je 24, jer se koristi podrazumijevana vrijednost za b i c

print(fun2(6, c = 11)) #pozivamo funkciju fun2 sa argumentom 6 i c = 11, i stampa se rezultat, a to je 22, jer se koristi podrazumijevana vrijednost za b, a c se postavlja na 11