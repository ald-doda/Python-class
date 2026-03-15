dict1 = {"a" : 50, "b" : 30, "c" : 40}
dict2 = {"b" : 20, "d" : 25}

for k in dict2.keys():
    if k in dict1.keys():
        dict1[k] += dict2[k]
    else:
        dict1[k] = dict2[k]

print(dict1)