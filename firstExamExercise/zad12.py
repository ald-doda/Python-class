def fun(x):
    return x//100%10

l = [12672, 28532, 29965, 33724]
l.sort(key=fun)
print(l[0])