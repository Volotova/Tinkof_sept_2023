n = int(input())
a, b, c, i, j, el, para = [], [], [], 0, 0, 0, -1
while i != n:
    k = int(input())
    a.append(k)
    i += 1
while j != n:
    k = int(input())
    b.append(k)
    j += 1
for x, y in zip(a, b):
    para += 1
    if x == y:
        continue
    else:
        c.append(para)
itog = a[c[0]:c[-1]+1]
itog.sort()
itog.reverse()
del a[c[0]:c[-1]+1]
for el in itog:
    a.insert(c[0], el)
if a == b:
    print("YES")
else:
    print("NO")