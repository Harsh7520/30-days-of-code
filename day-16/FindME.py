n = int(input())
a = list(map(int, input().split()))
t = int(input())
if t in a:
    print(a.index(t))
else:
    a.append(t)
    a.sort()
    print(a.index(t))
