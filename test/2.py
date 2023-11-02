a = input()
a = a.lower()
a = list(a)
all = []
all.append(a.count('s'))
all.append(a.count('h'))
all.append(a.count('e'))
all.append(a.count('r'))
all.append(a.count('i'))
all.append(a.count('f'))
if a.count('f') <= min(all):
    print(a.count('f')//2)
elif a.count('f') == 1:
    print(0)
else:
    print(min(all))