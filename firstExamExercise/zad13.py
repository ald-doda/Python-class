def fun(x):
    return str(x)[2:4]

l = [12673, 28532, 29985, 33724]
l.sort(key=fun, reverse=True)
print(l)
