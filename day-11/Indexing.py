n = int(input())
a = list(map(int, input().split()))
b = False
for i in range(len(a)-1):
    sta = a[:i]
    sto = a[i+1:]
    if(sum(sta)==sum(sto)):
        b = True
        k = i
        break
if b:
    print(k)
else:
    print(-1)
