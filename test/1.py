n, s = map(int, input().split())
b, i = [], 0
while i != n:
    a = int(input())
    if a > s:
        i += 1
    else:
        b.append(a)
        i += 1
if len(b) == 0:
    print(0)
else:
    b.sort()
    print(b[-1])
