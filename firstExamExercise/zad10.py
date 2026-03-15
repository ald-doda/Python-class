a = [1, 2, 3, 2, 1, 4, 3]
i = 0

while i < len(a):
    if a[i]  in a[i+1:]:
        a.pop(i)
    else:
        i += 1
    
print(a)